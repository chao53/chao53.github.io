---
title: Time Fall Tower        
cover: /TFT_cover.jpg
top: 9
d1: A roguelike game demo I developed 
d2: while participating in a MiniGame
d3: competition.
category: Highlighted
tags: 
  - Roguelike
  - Unity Engine
  - C#
date: 2024-08-20 16:15:43
---

This is a project I worked on while participating in a mini-game competition. Our development team consisted of six members, and I served as the lead programmer. I was responsible for developing the core framework of the game, which included a highly scalable RPG framework and the specific implementation of many character skills. The gameplay combines the combat and shopping system from Brotato with the synergy system of Auto Chess.



<iframe width="560" height="315" src="https://www.youtube.com/embed/DlvRSxrtf0Y?si=GUG7_o__ZCP7Mt_d" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



Download this demo:

https://github.com/chao53/Eric-s-Profile/releases/download/release/TimeFallTower.v1.0.zip



### My contributions

- The use of Data Asset


During the development of this project, I used custom DataAssets to store game data, which includes characters, weapons, enemies, levels, buffs, relics, and synergies. These DataAssets can be accessed directly by runtime scripts. 

<img src="https://chao53.github.io/images/tt_da.jpg" width="50%" height="50%">

Additionally, I wrote a tool that allows for one-click importing of data from Excel spreadsheets into DataAssets. 

<img src="https://chao53.github.io/images/tt_to.jpg" width="70%" height="70%">

This enables our project's planners to conveniently configure various game data directly within Excel.

<img src="https://chao53.github.io/images/tt_ex.jpg" width="70%" height="70%">

However, many skill mechanics cannot be implemented through numeric configuration alone. Therefore, I utilized subclass inheritance to realize the special effects of various skills, including buffs, relics, and synergies.

<table><tr>
<td><img src="https://chao53.github.io/images/tt_re.jpg" ></td>
<td><img src="https://chao53.github.io/images/tt_bu.jpg" width="80%" height="80%"></td>
<td><img src="https://chao53.github.io/images/tt_sy.jpg" width="90%" height="90%"></td>
</tr></table>
- The use of subclasses

During gameplay, these subclasses are dynamically added as components to the respective gameplay manager. For instance, when a synergy is activated, the synergy subclass component will be added to the synergy manager.

![](images/tt_sy2.jpg)

So as the relics.

![](images/tt_re2.jpg)

Finally, the managers collectively trigger the special effects of these subclasses.

![](images/tt_co.jpg)

- Internationalization

Initially, the game was available only in Chinese, but later I decided to add an English version. Due to the extensive amount of text in the game, I used a keyword replacement method to achieve internationalization. When players decide to switch languages, the program conducts a global search for strings in the game and replaces them with the corresponding language using a dictionary approach.

<img src="https://chao53.github.io/images/tt_tr.jpg" width="50%" height="50%">
