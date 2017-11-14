#!/bin/python3

import pygame as pg
import config as c
import color as col
from player import Player

pg.init()
screen = pg.display.set_mode(c.SIZE)
pg.display.set_caption(c.NAME)

player = Player()

done = False
clock = pg.time.Clock()
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("quit")
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                done = True
            elif event.key == pg.K_LEFT:
                player.move_left()
            elif event.key == pg.K_RIGHT:
                player.move_right()
            elif event.key == pg.K_UP:
                player.jump()
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.move_left_stop()
            elif event.key == pg.K_RIGHT:
                player.move_right_stop()
            elif event.key == pg.K_UP:
                player.jump_stop()

    screen.fill(col.BLACK)
    player.update()
    player.draw(screen)

    pg.display.flip()
    clock.tick(c.TICK)

pg.quit()
