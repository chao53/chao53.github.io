---
title: 其他工具合集
cover: /banner.jpg
top: 2
d1: 参加工作后为项
d2: 目团队开发的一
d3: 些工具
tags:
  - Tool
  - UE5
  - C++
  - Python
date: 2024-08-20 16:15:48

---

## 1、**UE5 自动化角色展示工具**

<iframe  width="560" height="315"  src="//player.bilibili.com/player.html?isOutside=true&aid=115348510611230&bvid=BV1BC47zcEju&cid=32962579828&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>



本工具是一个基于 Unreal Engine 5 的脚本化工具，用于为3D角色模型自动生成标准化的转盘展示视频。它通过自动化取代了手动设置场景、动画、渲染及后期的多步流程，旨在统一输出标准并提升工作效率。

**核心功能:**

- **自动化流程**：用户选择角色后，工具可自动执行从场景设置到视频生成的完整流程，无需人工干预。
- **程序化动画生成**：自动创建Level Sequence，并生成包含“摄像机环绕”和“角色自转”的转盘动画。
- **集成MRQ渲染与FFmpeg编码**：集成Movie Render Queue (MRQ)进行渲染，并调用FFmpeg将图像序列自动合成为视频文件（.mp4）。
- **参数化配置**：支持通过命令行传入参数，用于调整渲染预设、摄像机参数和视频编码选项，以支持CI/CD流程集成。



## 2、规范化贴图分辨率工具

工具入口: 在UTexture资产的右键菜单里的Texture Tools选项，可多选图片来批量处理。

<img src="https://chao53.github.io/images/1280X1280.PNG" width="70%" height="70%">

功能： 对错误分辨率的贴图进行自动规范化 缩放贴图至目标分辨率 按百分比缩放贴图 如：

1000x1500->1024x1024

2300x1000->2048x1024

<img src="https://chao53.github.io/images/tt12.jpg " width="70%" height="70%">

## 3、Groom头发导出XGen引导线ABC工具

工具入口: 在Groom资产的右键菜单里的Export GuideLine ABC选项

<img src="https://chao53.github.io/images/tt13.jpg " width="70%" height="70%">

点击后会弹出一个窗口，可以设置最小的曲线间隔。（数值越大，导出的引导线越稀疏）

<img src="https://chao53.github.io/images/get.png" width="70%" height="70%">

然后选择导出位置导出即可

ABC文件可直接导入maya 成曲线

<img src="https://chao53.github.io/images/gtxg.png" width="70%" height="70%">

