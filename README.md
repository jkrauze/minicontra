# minicontra
Homework project for "Python for Data Processing and Analysis" course.

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

### Play

Your goal in this game is to kill as many enemies as you can without get killed. Player starts with 3 health points. If got hurt, player looses 1 health point and get immortal for few seconds.

#### Controls

Player is able to move and aim (arrows by default), jump (`o` by default) and shoot (`p` by default). Jump while aiming down will move player down to a lower platform (not working on "ground").

## Levels are too short and boring...

You can modify levels easily using `vi`. For example, open `lvl/1.lvl` file
```
vi lvl/1.lvl
```
__If you never used `vi` before: to quit in panic press `ESC` and type `:q!`__

At first sight it looks like big mess. Without touching any other key type
```
:set nowrap
```
Now, use your imagination and make sure there are only `b`'s on 15th line and nothing below. For level creation you could use:
* `x` - player start position
* `b` - block; player can stand on it, but cannot go through it
* `p` - platform; player can stand on it and go through
* `s` - soldier enemy
* `l` - background rock

## I don't know what I'm doing here...

It's okay to get lost in the internet. Just exit this page. Or watch some [random video on YouTube](http://ytroulette.com "YouTube Roulette")

## External sources

To be generated on final release.
