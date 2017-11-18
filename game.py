import pygame as pg
import config as c
from level import Level
from menu import Menu


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
        self.actual_level = None

        self.done = False

    def run(self):
        while not self.done:
            option = Menu(self, "minicontra", ["Single player", "Two players", "Options", "Exit"]).run()
            if option == 0:
                while not self.done:
                    self.actual_level = Level(self, "lvl/1.lvl")
                    option = self.actual_level.run()
                    if option == 0:
                        option = Menu(self, "Game Over", ["Try again", "Return to menu", "Exit game"]).run()
                    else:
                        option -= 1
                    if option == 1:
                        break
                    elif option == 2:
                        self.done = True
            elif option == 3:
                break
        pg.quit()
