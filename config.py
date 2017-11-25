import color as col
import pygame as pg
import configparser


class Config:
    def __init__(self):
        self.file = 'settings.cfg'
        self.section = 'main'
        self.JUMP_PRECISION = 1.2
        self.NAME = 'minicontra'
        self.SIZE = [640, 480]
        self.TICK = 60
        self.BACKGROUND_COLOR = (5, 5, 30)
        self.KEY_UP = pg.K_UP, pg.K_w
        self.KEY_LEFT = pg.K_LEFT, pg.K_a
        self.KEY_DOWN = pg.K_DOWN, pg.K_s
        self.KEY_RIGHT = pg.K_RIGHT, pg.K_d
        self.KEY_JUMP = pg.K_o, pg.K_1
        self.KEY_SHOOT = pg.K_p, pg.K_2
        self.read()

    def read(self):
        self.config = configparser.RawConfigParser()
        self.config.read(self.file)
        self.NAME = self.config.get(self.section, 'name')
        self.SIZE = eval(self.config.get(self.section, 'size'))
        self.TICK = self.config.getint(self.section, 'tick')
        self.KEY_UP = eval(self.config.get(self.section, 'key_up'))
        self.KEY_LEFT = eval(self.config.get(self.section, 'key_left'))
        self.KEY_DOWN = eval(self.config.get(self.section, 'key_down'))
        self.KEY_RIGHT = eval(self.config.get(self.section, 'key_right'))
        self.KEY_JUMP = eval(self.config.get(self.section, 'key_jump'))
        self.KEY_SHOOT = eval(self.config.get(self.section, 'key_shoot'))

    def write(self):
        self.config.add_section(self.section)
        for name in ['NAME', 'SIZE', 'TICK', 'BACKGROUND_COLOR', 'JUMP_PRECISION', 'KEY_UP', 'KEY_LEFT', 'KEY_DOWN',
                     'KEY_RIGHT', 'KEY_JUMP', 'KEY_SHOOT']:
            self.config.set(self.section, name, eval(name))
        with open('settings.cfg', 'w') as file:
            self.config.write(file)
