#!/bin/python3

import pygame as pg
import config as c
import color as col
from player import Player
from block import Block

pg.init()
screen = pg.display.set_mode(c.SIZE)
pg.display.set_caption(c.NAME)


class Game:
    def __init__(self):
        self.player = Player()
        self.block = Block(100, 20, 80, c.SIZE[1] - 80)
        self.block_list = pg.sprite.Group()
        self.block_list.add(self.block)
        self.sprites_list = pg.sprite.Group()
        self.sprites_list.add(self.player)
        self.sprites_list.add(self.block)
        self.done = False
        self.clock = pg.time.Clock()

    def run(self):
        self.done = False
        while not self.done:
            self.tick()

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit")
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.done = True
                elif event.key == pg.K_LEFT:
                    self.player.move_left()
                elif event.key == pg.K_RIGHT:
                    self.player.move_right()
                elif event.key == pg.K_UP:
                    self.player.jump()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.player.move_left_stop()
                elif event.key == pg.K_RIGHT:
                    self.player.move_right_stop()
                elif event.key == pg.K_UP:
                    self.player.jump_stop()

        screen.fill(col.RED)
        self.sprites_list.update()
        self.sprites_list.draw(screen)

        if pg.sprite.spritecollide(self.player, self.block_list, False):
            print("COLLLISSIOSNNN!!!")

        pg.display.flip()
        self.clock.tick(c.TICK)


game = Game()
game.run()

pg.quit()
