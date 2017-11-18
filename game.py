import pygame as pg
import config as c
from player import Player
from block import Block
from enemy import Enemy


class Game:
    def __init__(self):
        pg.init()
        self.config = c.Config()
        self.screen = pg.display.set_mode(self.config.SIZE)
        pg.display.set_caption(self.config.NAME)

        self.block_list = pg.sprite.Group()
        self.bullets_list = pg.sprite.Group()
        self.enemies_list = pg.sprite.Group()
        self.sprites_list = pg.sprite.Group()

        self.player = Player(self, 0)
        Block(self, 100, 20, 180, self.config.SIZE[1] - 150)
        Block(self, 100, 20, 280, self.config.SIZE[1] - 120)
        Block(self, 1600, 20, 0, self.config.SIZE[1] - 20)
        Block(self, 1600, 20, 1700, self.config.SIZE[1] - 20)
        Block(self, 50, 90, 500, self.config.SIZE[1] - 140)
        Block(self, 50, 200, 100, self.config.SIZE[1] - 220)
        Enemy(self, 3, 100, 200)
        Enemy(self, 1, 200, 200)
        Enemy(self, 1, 290, 200)
        self.done = False
        self.clock = pg.time.Clock()
        self.skip = False

    def run(self):
        self.done = False
        while not self.done:
            self.tick()
        pg.quit()

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit")
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.done = True
                else:
                    self.player.handle_keydown(event.key)
            elif event.type == pg.KEYUP:
                self.player.handle_keyup(event.key)

        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.sprites_list.update()
        self.sprites_list.draw(self.screen)
        self.handle_shooting()

        pg.display.flip()
        self.clock.tick(self.config.TICK)

    def handle_shooting(self):
        for enemy in self.enemies_list:
            bullets = pg.sprite.spritecollide(enemy, self.bullets_list, False)
            for bullet in bullets:
                enemy.hp -= bullet.power
                bullet.kill()
                if enemy.hp <= 0:
                    enemy.kill()
