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
pip install --user pygame
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

To save your work, press `ESC` and type `:wq`.

## This game looks weird and sound is creepy...

All textures and sound samples used in this game has been found on [OpenGameArt](https://opengameart.org/). It's not easy to make good looking game using free to use sources. Despite this, I think that game looks and sounds nice. And all of external sources authors made a great work.

## This game works choppy as f...

As I wrote on the beginning, it's a simple game made as a homework. Lots of things can be optimized and made better. I'm aware of it.

## I don't see any turrets and there's only one type of level...

Huh... This game is only __inspired__ by Contra. It's not a remake. I see some space for improvements like turret enemies, player weapon powerups, horizontal levels... If you want to develop it, you are free to fork it.

## I don't know what I'm doing here...

It's okay to get lost in the internet. Just exit this page. Or watch some [random video on YouTube](http://ytroulette.com "YouTube Roulette").

## External sources

To be generated on final release.
