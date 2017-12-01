# minicontra

__minicontra__ is a simple game inspired by [Contra](https://en.wikipedia.org/wiki/Contra_(video_game "Wikipedia"), written in Python 3.6 using [pygame](https://www.pygame.org "pygame homepage") package. It was made as a homework project for "Python for Data Processing and Analysis" course on [Faculty of Mathematics and Information Science of Warsaw University of Technology](http://www.mini.pw.edu.pl). __This game has been created without any deeper knowledge about game developing. If you came here to learn something about pygame or platform game developing at all, it's not the best place. You have been warned.__

## How to play?

### Install Python 3.x with pygame
You should have Python 3.x installed on your system. To do this on [Fedora OS](https://getfedora.org/ "Get Fedora") you need to execute
```
sudo dnf install python3
```
You should have [pygame](https://www.pygame.org "pygame homepage") package installed also.
```
pip3 install --user pygame
```

### Run game
Just download or clone repository. Change working directory to __minicontra__ folder and run
```
./run.py
```
You should see a game window now. Native resolution for this game is 640x480. If it's too small for you, double it by changing video mode in options.

### Play

Your goal in this game is to kill as many enemies as you can without get killed. Player starts with 3 health points. If got hurt, player looses 1 health point and get immortal for few seconds. Each level ends when boss enemy is killed.

#### Controls

Player is able to move and aim (arrows by default), jump (`o` by default) and shoot (`p` by default). Jump while aiming down will move player down to a lower platform (not working on "blocks"; the yellow ones).

To change default controls you need to go to options menu, choose action for which you want to change key, press `Enter`, choose player for which you want to make change, press `Enter` again and as you will be asked to press some key, press that key you want to use for the action. Simple as that...

Every change in options will be automatically saved into `settings.cfg` file in main game directory. Configuration saved in this file is automatically read on game start also.

## Levels are too short and boring...

I'm not a game developer. If you have a feeling that you would have made it better (I'm sure you have...), just add some new levels or modify actual ones. Every `*.lvl` file in `lvl` directory will be automatically loaded.

### I don't know how to modify level...

You can add and modify levels easily using `vi`. For example, open `lvl/1.lvl` file
```
vi lvl/1.lvl
```
__If you never used `vi` before: to quit in panic press `ESC` and type `:q!`__

At first sight it looks like big mess. Without touching any other key type
```
:set nowrap
```
Now, press `i` and `Insert` key and release your imagination. Make sure there is nothing below 15th line. For level creation you could use:
* `x` - player start position
* `b` - block; player can stand on it, but cannot go through it; bullets cannot go through also
* `p` - platform; player can stand on it and go through; bullets also (bullets cannot stand on it of course...)
* `s` - soldier enemy
* `l` - background rock
* `f` - final boss

To save your work, press `ESC` and type `:wq`.

## This game looks weird and sound is creepy...

All textures and sound samples used in this game has been found on [OpenGameArt](https://opengameart.org/). It's not easy to make good looking game using free to use sources. Despite this, I think that game looks and sounds nice. And all of external sources authors made a great work.

## This game works choppy as f...

As I wrote on the beginning, it's a simple game made as a homework. Lots of things can be optimized and made better. I'm aware of it.

## I don't see any turrets and there's only one type of level...

Huh... This game is only __inspired__ by Contra. It's not a remake. I see some room for improvements like turret enemies, player weapon powerups, horizontal levels... If you want to develop it, you are free to fork it.

## I don't know what I'm doing here...

It's okay to get lost in the internet. Just exit this page. Or watch some [random video on YouTube](http://ytroulette.com "YouTube Roulette"). Or [less random ones](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw "3Blue1Brown channel").

## External sources

`./font/8-BIT WONDER.TTF`

https://www.dafont.com/8bit-wonder.font
```
Author: Joiro Hatgaya
Copyright:
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 VIEW THIS USING A MONOSPACED FONT!!!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 :: INTRODUCTION ::

  Greetings, welcome to the readme file for my fonts. That's it. :)

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 :: TERMS OF USE ::

  Currently all my fonts are freeware. That doesn't mean however, that you can
 do whatever you want with them. Here are the rules for use and distribution:

  1. You WILL NOT modify the fonts, the copyright notices, or this text file.
  2. You WILL NOT sell the fonts in ANY way.
  3. Whatever you do with it, you take full responsibility.

  Those are the rules you MUST follow to use or distribute these fonts. If you
 disagree, stop using the fonts immediately. If I grow aware of any violations
 of these terms, expect legal action to be taken. So, you have been warned.

  And, if you decide to use any of the fonts for commercial purposes, it would
 be really nice to receive a product sample. I can make a special version of a
 font exclusively for you as well. Just e-mail me if you are interested.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 :: ABOUT ME ::

  Well, not much to say, really. I'm a guy from Latvia, called Joiro Hatagaya,
 I like making fonts, 2D/3D graphics, music, games and programs and many other
 things. Send me feedback to make me happy and give me energy to do more. :)

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 :: CONTACT INFORMATION AND WEBSITES ::

 E-MAIL: JOIRO@HOTMAIL.COM | Please put "FONTS" in caps as the subject. Do not
 send spam, or you WILL regret it.

 WEBSITE: JOIRO.THE3DSTUDIO.COM | Come here to see some of my 3D work and find
 out what other things I do.

 NEW!!!
 FONT WEBSITE: http://www.typesource.com/Presents/Hatagaya/Fonts.html | Yes! I
 now have a special mini-website for my fonts only, where you can find all the
 latest versions of these fonts and also brand new fonts. So go visit it! NOW!

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 Revision: 1.20 | 05.01.2001
 [EOF]
```
`./img/11-Mid-Night.png`

http://www.bitday.me/
```
License: The Unlicense (http://unlicense.org/)
Author: Danny Care
```
`./img/ground3T.png`

https://opengameart.org/content/ground-tiles-0
```
License: CC0
Author: SpiderDave
```
`./img/01-Early-Morning.png`

http://www.bitday.me/
```
License: The Unlicense (http://unlicense.org/)
Author: Danny Care
```
`./img/OpenGunnerEnemySoldier.png`

https://opengameart.org/content/open-gunner-starter-kit
```
License: CC-BY 3.0
Author: Master484
Website: http://m484games.ucoz.com/
```
`./img/heart.png`

https://opengameart.org/content/heart-1616
```
License: CC-BY 3.0
Author: Nicole Marie T
Copyright: NicoleMarieProductions
```
`./img/OpenGunnerMechs.png`

https://opengameart.org/content/open-gunner-starter-kit
```
License: CC-BY 3.0
Author: Master484
Website: http://m484games.ucoz.com/
```
`./img/OpenGunnerHeroVer2.png`

https://opengameart.org/content/open-gunner-starter-kit
```
License: CC-BY 3.0
Author: Master484
Website: http://m484games.ucoz.com/
```
`./img/M484BulletCollection2.png`

https://opengameart.org/content/bullet-collection-2-m484-games
```
License: CC0
Author: Master484
Website: http://m484games.ucoz.com/
```
`./snd/Hit_02.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
`./snd/Hit_01.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
`./snd/Jingle_Lose_00.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
`./snd/game.ogg`

http://ozzed.net/music/8-bit-run-and-pun.shtml
```
Name: Shingle Tingle
Album: 8-bit Run 'n Pun
License: CC BY-SA 3.0
Author: Ozzed
Website: http://ozzed.net
```
`./snd/end.ogg`

http://ozzed.net/music/8-bit-run-and-pun.shtml
```
Name: Just a Minuet
Album: 8-bit Run 'n Pun
License: CC BY-SA 3.0
Author: Ozzed
Website: http://ozzed.net
```
`./snd/Jingle_Achievement_01.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
`./snd/Open_00.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
`./snd/menu.ogg`

http://ozzed.net/music/8-bit-run-and-pun.shtml
```
Name: Failien Funk
Album: 8-bit Run 'n Pun
License: CC BY-SA 3.0
Author: Ozzed
Website: http://ozzed.net
```
`./snd/Open_01.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
`./snd/Explosion_00.ogg`

https://opengameart.org/content/8-bit-sound-effects-library
```
License: CC-BY 3.0
Author: Little Robot Sound Factory
Website: www.littlerobotsoundfactory.com (not working on 30.11.2017)
```
