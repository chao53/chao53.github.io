---
title: UE5单镜头手势识别
cover: /MP_conver.jpg
top: 14
d1: 将谷歌的MediaPipe
d2: 解决方案，整合进UE5
d3: 里,以驱动MetaHuman
tags:
  - UE5
  - C++
  - Python
date: 2024-08-20 16:15:48
---



## 最终效果展示

集成为了一个UE5的plugin, 能方便的移植到各种项目

视频：
驱动骨骼

<iframe width="560" height="315" src="//player.bilibili.com/player.html?isOutside=true&aid=115348510613030&bvid=BV1qC47zcEiW&cid=32962577912&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

手势识别纠正



<iframe width="560" height="315" src="//player.bilibili.com/player.html?isOutside=true&aid=115348577721536&bvid=BV16q47zNEL7&cid=32963103410&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>



架构设计

![mediapipePipeLine](images\mediapipePipeLine.jpg)

UE5端通信总管HandDataReceiver  

## 实现详解

#### 一、 MediaPipe 本地部署并打包成 .exe

摆脱对用户本地Python环境的依赖

1. **选择嵌入式Python：** 使用Python官方的 **Embeddable Package**，这是一个轻量级的、绿色的Python运行时。

2. **依赖注入：** 通过 get-pip.py 为这个嵌入式环境安装 pip，然后精确地安装 mediapipe 和 opencv-python 两个核心依赖库。

3. **最终打包：** 使用 **PyInstaller** 将整个Python应用（包含脚本和所有依赖）打包成一个独立的 **.exe** 文件。这不仅封装了所有依赖，还隐藏了源码，并允许通过命令行参数向其传递配置信息（如端口号）。

4. **UE集成：** 在插件的 Build.cs 文件中，通过配置 **RuntimeDependencies**，实现了在UE项目打包时，能自动将此 .exe 文件包含到最终的游戏目录中。

   ![mpexe](images\mpexe.jpg)

#### 二、 构建UE5端数据接收层 (AX_HandDataReceiverActor)

在不影响游戏性能的前提下，稳定地接收高频数据，并优雅地管理外部进程

1. **进程管理与动态端口：**
   - 在C++中，通过 FPlatformProcess::CreateProc 启动 .exe。
   - 为了避免端口冲突，UE端首先在**端口0**上创建UDP Socket，操作系统会自动为其分配一个未被占用的端口。然后，这个**动态分配的端口号**被作为命令行参数传递给启动的 .exe 进程。这保证了系统在任何环境下都能稳定建立通信。
2. **多线程网络接收：**
   - 利用UE的 FUdpSocketReceiver，将UDP数据的接收和等待操作放在一个**独立的后台线程**中执行。这彻底避免了网络IO阻塞游戏主线程，保证了游戏的流畅运行。
3. **线程安全的数据交换：**
   - 后台线程接收到数据后，通过 AsyncTask(ENamedThreads::GameThread, ...) 异步任务，将解析好的数据**安全地派发**回游戏主线程。这是UE中进行多线程编程的标准、安全实践。
4. **健壮的路径管理：**
   - 为了解决了打包后找不到 .exe 的经典难题。通过C++预处理宏 #if WITH_EDITOR 区分编辑器和打包模式，并使用 FPaths::ConvertRelativePathToFull 将相对路径转换为绝对路径，确保了在任何启动环境下都能准确定位 .exe 文件。

#### 三、 解析数据并驱动骨骼 (自定义 AnimNode)

将离散的3D坐标点，转化为平滑、连续且符合骨骼层级结构的旋转动画

1. **封装算法：** 没有在动画蓝图的事件图表中用连线堆砌复杂的数学逻辑，而是创建了一个名为 **FAnimNode_HandPoseFromLandmarks** 的C++自定义动画节点。这使得动画蓝图异常整洁，所有复杂的计算都被封装在C++层。
2. **坐标空间变换：** 这是驱动骨骼的核心。所有计算都在正确的坐标空间中进行：
   - 从 HandData（组件空间）获取landmark点。
   - 获取每个骨骼的父骨骼在组件空间的变换 ParentTransform_CS。
   - 计算出目标方向向量 TargetDirection_CS。
   - 计算出骨骼在参考姿态（T-Pose）下的方向 RefDirection_CS。
   - 计算出从参考方向到目标方向的**旋转增量（Delta Rotation）**。
   - 将此增量正确地应用到骨骼的**局部空间（Local Space）**变换中。
3. **解决万向节死锁（Roll轴旋转丢失）：**
   - **[关键突破]** 意识到 FQuat::FindBetweenNormals 只能计算最短旋转路径，会丢失绕主轴的“扭转/Roll”信息，导致手腕X轴无法旋转。
   - 解决方案是利用**三个关键点**（如手腕、中指根、小指根）来定义一个**完整的3D坐标系**（Forward, Right, Up向量），而不仅仅是一个方向向量。
   - 通过这个坐标系构建一个无歧义的**目标旋转矩阵/四元数**，从而计算出包含完整Pitch, Yaw, 和Roll信息的旋转增量，完美解决了该问题。

​	





#### 四、 数据提纯与优化

从抖动、噪声丰富、甚至偶尔完全错误的 MediaPipe 数据中，提取出平滑、自然且符合生物力学的人体动作，同时如何避免“过度滤波”带来的响应迟滞

设计了一套多层次、逐步深入的数据净化管道。该管道从最粗粒度的“可信度”判断开始，到最细微的动画平滑结束，确保每一帧输出的姿态都是稳定且合理的。

#### 1. 置信度门槛（Confidence Gating）

MediaPipe 在进行推断时，会为检测到的每一只手提供一个**置信度分数（0.0 - 1.0）**。当手部姿态清晰时，分数很高（>0.9）；当手掌正对/背对镜头导致姿态模糊时，分数会显著下降。利用这个分数作为数据质量的**第一道关卡**。

- **实现方式：**
  - **数据采集端（Python）**：将 MediaPipe 输出的置信度分数与 landmark 坐标、左右手标签一同打包成 JSON，完整地发送给 Unreal Engine。
  - **数据接收端（C++ AnimNode）**：在动画节点 FAnimNode_HandPoseFromLandmarks 中，引入了一个可配置的 ConfidenceThreshold（置信度阈值）参数。
  - **过滤逻辑：** 在 Evaluate_AnyThread 函数的**最开始**，会检查传入的手部数据的置信度。如果分数**低于**设定的阈值，会认为这帧数据是**不可靠的“坏数据”**。节点将**完全丢弃**这帧数据，并直接输出上游传入的基础姿态（BasePose），使模型手部恢复到默认或由其他动画驱动的姿态。
- **优势：**
  - **从源头拦截错误：** 能有效防止因姿态识别困难（如手掌平放）导致的模型严重扭曲或“灵异”跳变。
  - **用户可控：** 开发者可以直接在动画蓝图的细节面板中实时调整阈值，以在**响应灵敏度**和**姿态稳定性**之间找到最佳平衡。

#### 2. 双阶段平滑机制（平滑处理）

在数据通过了置信度门槛，被确认为“可信”之后，对其进行双重平滑处理，以消除高频抖动。

- **阶段一（预处理平滑）**：
  - 在 FAnimNode_HandPoseFromLandmarks 中，接收到 landmark 数据后，首先进行一次轻度的 **指数滑动平均（EMA）** 平滑。
  - 使用自定义函数 GetSmoothedPoint()，对每个 landmark 的历史值做权重衰减式滤波。
  - 可通过 PreSmoothingAlpha 参数控制响应程度，数值越小越平滑，越大则越灵敏。
- **阶段二（动画应用平滑）**：
  - 在 FAnimNode_HandPoseFromLandmarks::Evaluate_AnyThread 中，每一个骨骼的最终局部旋转都会与上一次的结果进行 **Slerp（球面线性插值）** 平滑。
  - 这一层主要用于防止骨骼旋转的**视觉跳变**，尤其适用于动画系统中的 “惯性补偿”。
  - 通过 PostSmoothingAlpha 参数配置插值比例，提供用户级别的动画细节控制。

#### 3. 生物力学约束

为了让模型的动作更符合真实人体，对计算出的旋转施加了基于解剖结构的约束。

- **防止手指反向弯曲：**
  - MediaPipe 并不会主动判断手指弯曲的方向。
  - 在第二与第三节指关节（PIP 和 DIP）上，实现了基于**旋转分解与角度限制**的约束。
  - 将指关节的旋转增量分解为“摆动（Swing）”和“扭转（Twist）”两部分。丢弃扭转，然后计算出摆动的角度，并使用 FMath::Clamp 将其夹紧在一个符合生理的范围内（如 [-5°, 90°]），从而根除了手指向后翻的错误。

#### 4. 性能与开发辅助

- **动态数据复用与缓存：**
  - 使用 TMap 缓存骨骼的组件空间变换结果，避免在单次 Evaluate 调用中对同一骨骼进行重复的坐标空间转换，提升运行效率。
- **原始数据直通模式（开发辅助）：**
  - 提供 UseOriginData 开关，允许开发者绕过任何平滑、约束或限制，直接观察 MediaPipe 输出在模型上的原始映射效果。
  - 该模式特别适用于调试 landmark 方向、坐标轴映射和手指弯曲逻辑等底层问题。

![MediaPipeABP](images\MediaPipeABP.jpg)



### 五、手势识别纠正

训练一个能识别自定义的、独一无二的手势（如数字0-9、比心等）的高性能模型，并根据识别的手势，纠正动画

利用 **Google Colab** 的云端计算能力和 **MediaPipe Model Maker** 的迁移学习技术，实现了从数据采集到模型部署的全过程。

#### 1. 数据集工程化：高质量数据的采集与处理

深刻理解“数据决定模型上限”的原则，因此在数据准备阶段投入了大量精力，确保了数据集的**多样性**和**质量**。

- **自动化数据采集**:

  - 编写了一个功能强大的 **Python 批量处理脚本**。该脚本能自动遍历指定文件夹下的所有视频文件（.mp4, .mov 等）。

  - 对于每个视频，脚本会自动创建一个与视频文件名同名的文件夹，并以固定的帧率（可配置）从中提取图片。

    ![GestureTrain](images\GestureTrain.jpg)

- **构建多样化数据集**:

  - 为**数字0到9**、**点赞**、**比心**等十余种自定义手势，以及一个至关重要的**none（非手势）**类别，分别录制了视频。
  - 采集过程充分考虑了多样性，涵盖了**不同的人物、角度、光照和背景**，以增强模型的泛化能力。
  - 特别是 none 类别，采集了大量手部在移动、放松、以及手势切换过程中的“中间态”图片，以训练模型在非交互状态下保持“沉默”，避免误识别。

#### 2. 云端训练：利用 MediaPipe Model Maker 实现高效迁移学习

在本地配置复杂的深度学习环境（CUDA, cuDNN）既耗时又容易出错，且对硬件要求高。

于是将整个训练流程迁移到了 **Google Colab** 云端平台。

- **环境零配置**: 直接利用 Colab 预置的、带免费 GPU 加速的 Python 环境，无需任何本地安装。

- **稳定的数据流**: 为了解决 Colab 上传大文件时容易中断的问题，采用了**“Google Drive 中转”**的方案：先将打包好的数据集 .zip 文件上传到 Google Drive，然后在 Colab 中挂载 Drive，并高速复制到本地环境再解压。这套流程被证明是极其稳定和高效的。

- **迁移学习**: 没有从零开始训练模型。**MediaPipe Model Maker** 在后台自动加载了 Google 预训练的、强大的**手部特征提取基础模型**，只需在其之上，用自己的数据集来微调（Fine-tuning）一个全新的、为自定义手势量身定做的分类头。这使得训练过程不仅速度飞快（通常在十几分钟内完成），而且模型起点高，准确率非常有保障。

  ![GoogleTrain](images\GoogleTrain.jpg)

#### 3. 端到端部署与交互

训练完成后，将定制化的 .task 模型集成回的系统中，打通了从识别到交互的最后一环。

- **Python 端升级**:
  - 将原有的 Hands 模型完全替换为新的、功能更强大的 **GestureRecognizer**。它不仅能提供与之前完全一致的坐标、左右手标签和置信度数据，还额外输出了刚刚训练的**自定义手势标签**（如 "Thumb_Up", "Heart", "One", "Two" 等）。
  - 所有这些信息被实时打包成 JSON，通过 UDP 发送给 UE。
  
- **UE 端接收与响应**:
  
  - C++ AX_HandDataReceiverActor 负责解析新增的 Gesture 字段。
  
  - 在动画蓝图或行为树中，可以轻松地获取到这个手势字符串，并用一个简单的 Switch on String 节点来分发逻辑。
  
    

![MP_train](images\MP_train.jpg)
