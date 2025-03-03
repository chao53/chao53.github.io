---
title: Time Fall Tower        
cover: /TFT_cover.jpg
top: 9
d1: 我在参加MiniGame
d2: 比赛时开发的一个
d3: 肉鸽游戏
category: Highlighted
tags: 
  - Roguelike
  - Unity Engine
  - C#
date: 2024-08-20 16:15:43
---

**Project name: ** Time Fall Tower   

**Date of completion:**  Sept 4, 2023

**Software used:** Unity

**My role:** Designer/ Main Programmer



这是我在参加一场小游戏竞赛时所做的项目。我们的开发团队由六名成员组成，我担任了首席程序员。我负责开发游戏的核心框架，其中包括一个高度可扩展的RPG框架以及许多角色技能的具体实现。游戏玩法结合了《土豆兄弟》的战斗和购物系统，以及自走棋的羁绊系统。

视频：

<iframe width="560" height="315" src="//player.bilibili.com/player.html?bvid=BV1JUP5e3Eds&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>



下载试玩:

https://github.com/chao53/Eric-s-Profile/releases/download/release/TimeFallTower.v1.0.zip



### 我的贡献

- Data Asset的应用


在这个项目的开发过程中，我使用了自定义的DataAssets来存储游戏数据，包括角色、武器、敌人、关卡、增益效果、遗物和协同效果。这些DataAssets可以通过运行时脚本直接访问。

<img src="https://chao53.github.io/images/tt_da.jpg" width="50%" height="50%">

此外，我还编写了一个工具，可以一键将数据从Excel表格导入到DataAssets中。

<img src="https://chao53.github.io/images/tt_to.jpg" width="70%" height="70%">

这使得我们项目的策划人员可以方便地直接在Excel中配置各种游戏数据。

<img src="https://chao53.github.io/images/tt_ex.jpg" width="70%" height="70%">

然而，许多技能机制无法仅通过数字配置实现。因此，我利用了子类继承来实现各种技能的特效，包括buff效果、遗物和羁绊效果。

<table><tr>
<td><img src="https://chao53.github.io/images/tt_re.jpg" ></td>
<td><img src="https://chao53.github.io/images/tt_bu.jpg" width="80%" height="80%"></td>
<td><img src="https://chao53.github.io/images/tt_sy.jpg" width="90%" height="90%"></td>
</tr></table>
- 对子类继承的应用

在游戏过程中，这些子类会作为组件动态地添加到相应的游戏管理器中。例如，当一个协同效果被激活时，羁绊效果子类组件将被添加到协同效果管理器中。

![](images/tt_sy2.jpg)

遗物同理

![](images/tt_re2.jpg)

最后，管理器会共同触发这些子类的特效。

![](images/tt_co.jpg)

- 国际化

最初，游戏仅提供中文版本，但后来我决定添加英文版本。由于游戏中有大量文本，我采用了关键词替换的方法来实现国际化。当玩家决定切换语言时，程序会在游戏中进行全局字符串搜索，并使用字典方法将其替换为相应的语言。

<img src="https://chao53.github.io/images/tt_tr.jpg" width="50%" height="50%">
