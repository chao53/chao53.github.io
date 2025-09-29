---
title: Maya系列工具
cover: /crowed_cover.png
top: 11
d1: 包括模型检查,美术生
d2: 产流水线,自动化生成
d3: 和实用功能等工具
tags:
  - DCCTool
  - Maya
  - Python
  - Mel
date: 2024-08-20 16:15:48
---

## 一、说明

此工具只适用于maya2023



## 二、安装方法

![img](images\installMaya.jpg)

安装后如果发现工具还是旧版本可以重启maya再安装

## 三、X_Tool实用工具

### 1、网格体导出简单绑定工具

选择要导出的网格体，点击导出简单绑定即可



并非蒙皮，只是导出成带一根骨骼的fbx, 为了在UE里看骨骼网格体的效果

### 2、路径修复工具

#### 功能1：修复当前文件的引用



- 点击打开文件路径编辑器 可以打开文件路径编辑器，可以看到当前文件中丢失的路径

![img](images\filept1.jpg)

- 点击浏览可以选择一个路径。默认为maya文件同级的Texture文件夹。
- 点击"用指定路径修复文件引用"即可用上面选择的路径替换掉丢失的路径（前提是选择的路径有效）

![img](images\filept2.jpg)

#### 功能2: 将当前文件引用的文件归拢到相对路径



- 点击"复制引用文件到指定路径" 可以将没有丢失的引用文件，复制到 上面选择的路径（一般默认为同路径下的 Texture文件夹，与SVN归档规则相同）。

### 3、不对称点查找工具

![Asym](images\Asym.jpg)

先选中要检查的物体，再点击找到模型的不对称点 就可以选中不对称的点。

## 四、模型检查工具

![img](images\check1.jpg)

点击check的按钮打开工具

视频:

maya_modelcheck

模型检查工具中的第一栏会显示工具检查标准的更新时间，工具检查标准即为X_TOOL目录下的config_data.xlsx

其作用是配置模型检查标准的细节数据。比如角色设定的身高数据

![img](images\check2.jpg)

![img](images\check3.jpg)

如果这些数据有更新，可以点击模型检查工具UI里的 "更新检查标准数据文件"，然后选择新版本的config_data.xlsx 来完成更新。

下方，会显示当前角色的名字，角色名字在maya文件名中提前，命名规则为SM_角色名。 不符合规则或未保存的文件无法识别，会让检查出错。

再下方，是详细的模型检查项目，可以点击"检查"按钮，来对单个项目进行检查，也可以，点击一键检查来检查所有项目。

下面是对每个检查项目的说明。

### 1、角色身高是否符合原画设定

config_data.xlsx中的相关配置：

表"基本配置" 中的身高检查容差

![img](images\tollerant.jpg)

表"角色身高" 中各个角色的具体身高设定，第一列为角色名，第二列为身高

![img](images\check4.jpg)

点击检查后，会显示身高差，在容差之内会视为通过

![img](images\check5.jpg)

注意：带绑定的角色检查的身高会不准确。只适用于未绑定的mesh

### 2、检测模型是否在地面网格上方

![img](images\check6.jpg)

检测是否有物体低于地平面

### 3、模型面数检查工具

![img](images\check7.jpg)

只能识别按规范命名的模型。

### 4、检查大于四边面

![img](images\check8.jpg)

单独检查该项，能选中大于四边的面

### 5、检查废点废面

![img](images\chekc9.jpg)

单独检查该项，能选中废点废面

### 6、检查网格体是否左右对称

![img](images\check10.jpg)

会显示有不对称点的物体。 在X_Tool中能选中这些不对称的点

![img](images\check11.jpg)

### 7、检查网格体命名

![img](images\check12.jpg)

命名规则[Maya 模型命名规范](https://dztkd8r9io.feishu.cn/docx/V7m5dUyNqoFDSFxoAwqcXxnQnhe?from=from_copylink)

### 8、检查UV集命名

![img](images\check13.jpg)

只允许有一个叫map1的uv集

### 9、检查眼球UV是否有反转

![img](images\check14bt.jpg)

![img](images\eyeUV.jpg)

在uv编辑器里看到是红色的uv就是反转的

### 10、检查Body的拓扑是否与Metahuman 的Body一致

![img](images\Check14.jpg)

## 五、工作流工具

### 1、标准化命名工具

视频：

maya_SVN

会重命名部件与部件的第一个材质

### 2、SVN工具

第一次提交要 手动选择SVN根目录。

角色模型文件归档svn分支:svn://172.27.190.188/3D_Assets

提交的目录是根据maya文件命名来解析的，所以建议先用重命名工具标准化命名

若勾选同时上传引用文件，会把引用的文件归拢到SVN目录maya文件同级的Texture文件夹

- 正常来说，直接点击 “复制并上传到SVN” 即可
- 如果服务器有更新，可以先点击“更新整个SVN仓库”更新



如果出现如下图的提示

![img](images\svnToolWarn.jpg)

则需要按以下步骤操作

1，重新运行SVN安装程序

2，点击Modify

![img](images\svnIns2.jpg)

3，command line client tools 这个要选择第一项

![img](images\svnIns.jpg)

4，后面一路默认继续重新安装就行

5，重启maya

## 六、PoseWrangler Solver 自动化创建工具

![img](images\poseTBt.jpg)

![img](images\pstool.jpg)

### 1、打开PoseWranger

如果有安装，可以通过这个按钮打开PoseWranger

### 2、重新创建全部Solver

会把原有的Solver 全删掉并创建本项目需要的Solvers ， 如下图

![img](images\poseWrangler.jpg)

### 3、重建Solver并保留原有数据

会先读取 各个Pose在 原有Solver下的 Driven transform 数据，并在创建Solver后赋值

需要再原本就要Solver 数据的情况下执行

### 4、为选中模型的每个Pose添加BS

要先选择一个或多个Mesh, 再点击此按钮。

点击后会根据每个pose 生成BlendShape

![0](images\bswin.jpg)



## 七、Livelink面部数据传输工具

![img](images\llb.png

#### 1、模式1：直接驱动BlendShape

打开工具会自动获取场景内的BS。 也可以手动选择模型，来指定特定的受驱动BS

![llb2](images\llb2.png)

#### 2、模式2：先建立控制器，再进行livelink数据驱动

![llb3](images\llb3.png)

先点击导入控制面板，

然后选择要驱动的模型，点击约束到控制器。

![llb4](images\llb4.png)

#### 3、livelink 连接

能够自动识别与手机连接的局域网ip. 若不对可以手动选择，或填入

保证手机端livelink的ip和端口与工具显示的相同，点击开始连接即可

若要停止连接，请点击停止连接，否则可能会导致端口占用



视频：livelinkmaya



## 八、实验性工具

### 1、卡片头发生成工具

![img](images\GHBut.jpg)

![img](images\XGen.jpg)

视频:maya_XGenCard

