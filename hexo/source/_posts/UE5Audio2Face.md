---
title: UE5 Audio2Face音频驱嘴型插件
cover: /a2fc.jpg
top: 6
d1: 将英伟达的Audio2Face 
d2: 编译出的SDk。以第三方
d3: 库的形式接入UE5
tags:
  - UE5
  - C++
  - Solution
date: 2024-08-20 16:15:48

---

开发背景： 在2025年10月1日 英伟达弃用了旧有的 omniverse 框架。 同时开源了 Audio2Face的代码。此时官方的UE5插件需要链接为服务器，才能驱动动画，不符合项目需求。于是我从编译Audio2Face SDK 开始，从头把A2F接入UE5，开发了这个插件 。



视频：

<iframe width="560" height="315" src="//player.bilibili.com/player.html?isOutside=true&aid=115540978832050&bvid=BV16fCWBGEfX&cid=33967705229&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>



**核心功能**

- 集成 NVIDIA Audio2Face C++ SDK，在 Unreal Engine 中通过音频实时生成高保真面部动画。
- 支持两种驱动模式：
  1. **实时驱动**：通过麦克-风输入，实时捕捉音频并驱动角色面部表情。
  2. **文件驱动**：使用预录制的 .wav 音频文件，生成与音频精确同步的面部动画。

**技术特性**

- **模型支持**：支持加载由 NVIDIA Omniverse Audio2Face 应用生成的标准模型文件（model.json）。
- **蓝图接口**：提供简洁的蓝图节点，开发者和美术师可通过 StartCapture（开始麦克风捕捉）和 PreProcessAndPlay（播放音频文件）等函数轻松调用插件功能。
- **动画系统集成**：通过自定义动画节点（AnimNode）无缝集成至UE的动画蓝图（Animation Blueprint），将生成的表情数据应用于任何角色骨骼网格体。
- **参数化控制**：支持在运行时动态调整面部动画的各项参数，如表情强度、平滑度、眼睑和嘴唇偏移等，以实现对最终效果的精细控制。
- **音频处理**：内置音频处理管线，自动将输入的音频（多声道、任意采样率）转换为A2F引擎所需的格式（单声道、16kHz）。

**第三方库集成**

- **SDK编译与集成**：插件的核心功能基于 NVIDIA Audio2Face C++ SDK。SDK源码被编译成动态链接库（DLL），并作为第三方模块集成到插件中。

  <img src="https://chao53.github.io/images/a2f.jpg" width="66%" height="66%">

- **依赖管理**：所有必需的运行时依赖项，包括编译后的SDK库、NVIDIA CUDA 运行时库、TensorRT 库以及 miniaudio 库，均已包含在插件的 ThirdParty 和 Binaries 目录中，无需用户手动安装。

- **跨平台音频**：使用轻量级 miniaudio 库处理底层音频捕捉，确保低延迟和跨平台兼容性。

**工作流程**

1. 将插件提供的 AudioCaptureComponent（用于实时）或 AudioCurveSourceComponent（用于文件）添加到场景中的 Actor 上。
2. 在组件的细节面板中，指定要使用的A2F模型目录。
3. 在动画蓝图中，添加 X_Audio2Face 动画节点，并将其连接到最终姿势输出。
4. 通过蓝图或C++调用相应组件的函数，启动音频处理和动画生成。