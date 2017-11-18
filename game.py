import pygame as pg
import config as c
from level import Level


class Game:
    def __init__(self):
        pg.init()
        self.config = c.Config()
        self.screen = pg.display.set_mode(self.config.SIZE)
        pg.display.set_caption(self.config.NAME)

        self.block_list = pg.sprite.Group()
        self.player_bullets_list = pg.sprite.Group()
        self.enemies_list = pg.sprite.Group()
        self.sprites_list = pg.sprite.Group()

        self.level = Level(self, "lvl/1.lvl")
        self.done = False

    def run(self):
        self.level.run()
        pg.quit()
