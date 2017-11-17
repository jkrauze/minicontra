import color as col
import pygame as pg

NAME = 'minicontra'
SIZE = [800, 600]
TICK = 60
BACKGROUND_COLOR = col.BLACK
JUMP_PRECISION = 1.2

KEY_UP = pg.K_UP, pg.K_w
KEY_LEFT = pg.K_LEFT, pg.K_a
KEY_DOWN = pg.K_DOWN, pg.K_s
KEY_RIGHT = pg.K_RIGHT, pg.K_d
KEY_JUMP = pg.K_o, pg.K_1
KEY_SHOOT = pg.K_p, pg.K_2