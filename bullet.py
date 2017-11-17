import pygame as pg
import config as c
import color as col


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, width, height, speed, x, y, way):
        super().__init__()
        self.game = game
        self.width = width
        self.height = height
        self.speed = speed
        self.way = way
        self.image = pg.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = col.WHITE
        self.image.fill(self.color)

    def update(self):
        self.rect.x += self.speed * self.way[0]
        self.rect.y += self.speed * self.way[1]
        if pg.sprite.spritecollide(self, self.game.block_list, False):
            self.kill()
