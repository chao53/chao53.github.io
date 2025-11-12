---
title: Evalution
cover: /Evolution_cover.png
d1: 我在腾讯实习时 
d2: 参与开发的一个
d3: 动作游戏。
top: 20
category: Highlighted
tags:
  - Game
  - UE5
  - C++
date: 2024-08-20 16:15:44
---

**Project name:** Evalution

**Date of completion:**  Jan 1, 2023

**Software used:** Unreal Engine5

**My role:** Designer/ Main Programmer



在腾讯实习期间，我参与了一个动作游戏演示的开发。在这个小团队（除了外包的美术，团队共有三人）中，我负责设计和实现玩家角色的3Cs（控制、相机和角色）、战斗系统和游戏框架。我开发了一个基于标签的技能系统，这简化了传统状态机中固有的复杂性，并利用动画通知来确保角色动画中的平滑过渡和连击序列。此外，我还花了大量精力优化控制响应性和动画呈现，包括整合详细的腿部和上半身动作。我还负责从《古墓丽影》、《怪物猎人》和《艾尔登法环》等游戏中提取和重现资源，以协助我们的美术团队进行生产工作。



Gameplay demo 视频：

<iframe width="560" height="315" src="//player.bilibili.com/player.html?isOutside=true&aid=114099480435919&bvid=BV1gS96YgETz&cid=28675737292&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

此demo的更多细节 视频：

<iframe width="560" height="315" src="//player.bilibili.com/player.html?bvid=BV1JSP5e6ENP&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

### 相关技术

- 场景同步

我们的项目团队利用云技术在云端计算机上渲染高精度场景，然后将本地游戏场景与渲染端进行同步。这显著提升了游戏性能。

<img src="https://chao53.github.io/images/ezgif.gif" width="70%" height="70%">





### 我的贡献

- 基于标签的技能系统

我开发了一个基于游戏标签和动画通知的动画系统，取代了传统的状态机。这使得系统更容易维护和扩展。该系统在实现攻击连击和优先处理击中中断动作方面表现出色。

通过使用动画通知状态来配置连击动作，当动画到达通知状态窗口时，如果接收到输入，它将过渡到相应的新动画。

<img src="https://chao53.github.io/images/Ev_Ac.jpg" width="70%" height="70%">

.

<img src="https://chao53.github.io/images/Ev_Ac2.jpg" width="70%" height="70%">

- fullbody Ik的应用


<table><tr>
<td><img src="https://chao53.github.io/images/ev_ik.png" ></td>
<td><img src="https://chao53.github.io/images/ev_ik2.png" width="85%" height="85%"></td>
</tr></table>


- animation blending 和 Aim Offset 的应用 

通过在骨骼的盆骨处将上半身和下半身分开，我将弓箭手射击的上半身动画与下半身的移动动画结合起来。实现弓箭手在移动时丝滑射击的动画效果。

<img src="https://chao53.github.io/images/ev_bl.png" width="70%" height="70%">

一般来说，移动动画使用混合空间来覆盖四个方向的各种地面动作。然而，对于原地转向动作，根运动需要使用蒙太奇（montages）。播放一个蒙太奇可能会中断另一个蒙太奇，因此使用UE5的“Animation Slot Groups”非常重要。当这些槽被设置为不同的组时，可以防止中断，并允许同时播放多个蒙太奇。例如，将弓箭动作的蒙太奇数据设置在“上半身”槽中，而将原地转向的蒙太奇设置在“下半身”槽中，这样就可以无缝地整合不同的身体运动动画。

<img src="https://chao53.github.io/images/ev-mt.png" width="70%" height="70%">

当玩家的控制器开始旋转时，计算控制器旋转角度与角色朝向之间的差值。如果差值超过90度，则触发转向蒙太奇（turning montage）。

<img src="https://chao53.github.io/images/ev-tr1.png" width="70%" height="70%">

在角色蓝图中，检查每一帧，看看偏移角度的绝对值是否大于90度。如果是，则进入旋转状态，并根据该值是否大于0，选择播放左转或右转动画。

<img src="https://chao53.github.io/images/ev-tr2.png" width="70%" height="70%">



- 使用 Behavior Tree来构建敌人AI.

在实现敌人AI行为树时，首先获取玩家的当前位置。然后，AI根据玩家的相对位置选择靠近玩家或攻击玩家。

<img src="https://chao53.github.io/images/ev_bt1.jpg" width="70%" height="70%">

为了降低游戏难度并增强可玩性，敌人被赋予了耐力值。根据耐力值的不同，AI在快速接近或缓慢移动向玩家之间做出选择。快速接近会更快消耗耐力条。当耐力耗尽时，敌人将更慢地向玩家移动。

<img src="https://chao53.github.io/images/ev_bt2.jpg" width="70%" height="70%">

在攻击玩家时，敌人AI根据与玩家的距离选择攻击方式。在远程时，它投掷巨石；在中距离时，它向前冲刺；在近距离时，它用爪子攻击或咬人。这些攻击有多种变化，AI会随机选择。此外，每个攻击都有冷却时间，以防止同一动作重复执行过于频繁。

- UI 设计

UI系统是使用Unreal Engine的Widget  Blueprint和自定义UI事件系统构建的。该设置允许在游戏过程中进行动态更改，例如切换武器或执行连击时，武器图标会更新。类似地，瞄准镜会随着弓箭蓄力时间的变化而变化。玩家和Boss的生命值和耐力条会根据来自玩家和敌人蓝图的数据实时更新。

<img src="https://chao53.github.io/images/ev_ui.jpg" width="70%" height="70%">
