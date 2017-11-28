import pygame as pg
import os
import config as c
from level import Level
from menu import Menu


class Game:
    def __init__(self):
        pg.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=512)
        pg.init()
        self.config = c.Config()
        self.screen = pg.display.set_mode(self.config.SIZE)
        pg.display.set_caption(self.config.NAME)

        self.ground_sprite = pg.image.load(os.path.join('img', 'ground3T.png'))
        self.ground_sprite.set_colorkey(self.ground_sprite.get_at((17, 1)))
        self.ground_sprite = pg.transform.scale2x(self.ground_sprite)

        self.player_sprite = pg.image.load(os.path.join('img', 'OpenGunnerHeroVer2.png')).convert()
        self.player_sprite.set_colorkey(self.player_sprite.get_at((1, 1)))

        self.enemy_sprite = pg.image.load(os.path.join('img', 'OpenGunnerEnemySoldier.png')).convert()
        self.enemy_sprite.set_colorkey(self.enemy_sprite.get_at((1, 1)))

        self.bullet_sprite = pg.image.load(os.path.join('img', 'M484BulletCollection2.png')).convert()
        self.bullet_sprite.set_colorkey(self.bullet_sprite.get_at((1, 1)))

        self.background = pg.image.load(os.path.join('img', '11-Mid-Night.png'))
        self.background.set_alpha(64)

        self.menu_background = pg.image.load(os.path.join('img', '01-Early-Morning.png'))
        self.menu_background.set_alpha(128)

        self.background_list = pg.sprite.Group()
        self.block_list = pg.sprite.Group()
        self.player_bullets_list = pg.sprite.Group()
        self.enemies_list = pg.sprite.Group()
        self.players_list = pg.sprite.Group()
        self.sprites_list = pg.sprite.Group()
        self.actual_level = None

        self.done = False

    def run(self):
        while not self.done:
            pg.mixer.music.load(os.path.join('snd', 'menu.ogg'))
            pg.mixer.music.play(-1)
            option = Menu(self, self.config.NAME, ["Single player", "Two players", "Options", "Exit"], -1).run()
            if option == 0:
                while not self.done:
                    pg.mixer.music.stop()
                    self.actual_level = Level(self, "lvl/1.lvl")
                    option = self.actual_level.run()
                    if option == 0:
                        option = Menu(self, "Game Over", ["Try again", "Return to menu", "Exit game"], -1).run()
                    else:
                        option -= 1
                    if option == 1:
                        break
                    elif option == 2:
                        self.done = True
            elif option == 3:
                break
        pg.quit()
