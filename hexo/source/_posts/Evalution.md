---
title: Evalution
cover: /Evolution_cover.png
d1: An action game demo I worked on 
d2: for one year during my internship
d3: at Tencent.
top: 10
category: Highlighted
tags:
  - AAA
  - Unreal Engine5
  - C++
date: 2024-08-20 16:15:44
---





During my internship at Tencent, I was involved in the development of a AAA action game demo. In this small team (three members, excluding art outsourcing), I was responsible for designing and implementing the player character's 3Cs, combat systems, and gameplay framework. I developed a tag-based skill system that simplified complexities inherent in traditional state machines, and utilized animation notifies to ensure smooth transitions and combo sequences in character animations. Moreover, I devoted significant effort toward optimizing control responsiveness and animation presentation, including the integration of detailed leg and upper body movements. I also managed the extraction and reproduction of assets from games such as "Tomb Raider," "Monster Hunter," and "Elden Ring" to assist our art team in their production work.



Gameplay demo：



<iframe width="560" height="315" src="https://www.youtube.com/embed/KSs88ZWBxKk?si=Iws1Z4SNWoMYQvNL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



Here are some details of this demo：



<iframe width="560" height="315" src="https://www.youtube.com/embed/wVoykDmwZ_0?si=aSCT2DrsYaP9wVMQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>





### Some technologies used in the project

- Scene synchronization technology

Our project team utilized cloud technology to render high-precision scenes on cloud computers, and then synchronized the local gameplay scenes with the rendering end. This significantly enhanced the game performance.

![](images/ezgif.gif)





### My contributions

- A tag-based skill system

I developed an animation system based on gameplay tags and animation notifications, replacing the traditional state machine. It is easier to maintain and expand. This system excels in implementing attack combos and prioritizing hit interrupt actions.

Using animation notify states to configure combo moves, when the animation reaches the notify state window, if an input is received, it will transition to the corresponding new animation.

<img src="https://chao53.github.io/images/Ev_Ac.jpg" width="70%" height="70%">

.

<img src="https://chao53.github.io/images/Ev_Ac2.jpg" width="70%" height="70%">

- The application of full-body IK (Inverse Kinematics)


<table><tr>
<td><img src="https://chao53.github.io/images/ev_ik.png" ></td>
<td><img src="https://chao53.github.io/images/ev_ik2.png" width="85%" height="85%"></td>
</tr></table>


- The use of animation blending and Aim Offset. 

By dividing the skeleton into upper and lower bodies at the pelvis, I combine an upper body animation of an archer shooting with a lower body locomotion animation. This creates a seamless animation of an archer shooting while moving.

![](images/ev_bl.png)

In general, locomotion animations use a blend space to cover various ground movements in four directions. However, for turning-in-place actions, root motion requires montages. Playing a montage can interrupt another, so using UE5’s "Animation Slot Groups" is essential. These slots, when set to different groups, prevent interruptions and allow simultaneous playback of multiple montages. For example, setting the archery montage data on the 'upper body' slot and the turning-in-place montage on the 'lower body' slot facilitates seamless integration of different body movement animations.

![](images/ev-mt.png)

When the player's controller begins to rotate, calculate the difference between the angle of the controller's rotation and the character's orientation. If the difference exceeds 90 degrees, trigger the turning montage.

![](images/ev-tr1.png)

In the character blueprint, check each frame to see if the absolute value of the offset angle is greater than 90 degrees. If it is, enter the rotating state, and depending on whether the value is greater than 0, choose to play either the left-turn or right-turn animation.

![](images/ev-tr2.png)



- Use a Behavior Tree to construct enemy AI.

When implementing the enemy AI behavior tree, it first retrieves the player's current position. The AI then chooses between approaching or attacking the player based on their relative location.

<img src="https://chao53.github.io/images/ev_bt1.jpg" width="70%" height="70%">

To reduce game difficulty and enhance playability, enemies are assigned a stamina value. Depending on this stamina, the AI chooses between quickly approaching or slowly moving toward the player. Rapid approaches deplete the stamina bar faster. When the stamina is exhausted, the enemy will move towards the player more slowly.

<img src="https://chao53.github.io/images/ev_bt2.jpg" width="70%" height="70%">

When attacking the player, the enemy AI selects its attack method based on the distance to the player. At long range, it throws boulders; at medium range, it lunges forward; and at close range, it claws or bites. These attacks have several variations, which the AI chooses randomly. Moreover, each attack has its cooldown period to prevent the same action from being repeated too frequently.



- UI design

The UI system is built using Unreal Engine's Widget Blueprint and a custom UI event system. This setup allows for dynamic changes during gameplay, such as the weapon icon updating when weapons are switched or combos are executed. Similarly, the reticle changes with the bow’s charge time. Health and stamina bars for both the player and the boss are updated in real-time based on data from player and enemy blueprints.

![](images/ev_ui.jpg)
