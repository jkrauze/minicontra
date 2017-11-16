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
        self.player = Player(self)
        self.block_list = pg.sprite.Group()
        self.block_list.add(Block(100, 20, 180, c.SIZE[1] - 150))
        self.block_list.add(Block(100, 20, 280, c.SIZE[1] - 120))
        self.block_list.add(Block(1600, 20, 0, c.SIZE[1] - 20))
        self.block_list.add(Block(1600, 20, 1700, c.SIZE[1] - 20))
        self.block_list.add(Block(50, 200, 500, c.SIZE[1] - 250))
        self.block_list.add(Block(50, 200, 100, c.SIZE[1] - 220))
        self.sprites_list = pg.sprite.Group()
        self.sprites_list.add(self.player)
        for block in self.block_list:
            self.sprites_list.add(block)
        self.done = False
        self.clock = pg.time.Clock()
        self.skip = False

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

        screen.fill(c.BACKGROUND_COLOR)
        self.sprites_list.update()
        self.sprites_list.draw(screen)

        pg.display.flip()
        self.clock.tick(c.TICK)


game = Game()
game.run()

pg.quit()
