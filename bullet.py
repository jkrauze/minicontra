import pygame as pg
import config as c
import color as col


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, width, height, speed, power, x, y, way):
        super().__init__()
        self.game = game
        self.game.player_bullets_list.add(self)
        self.game.sprites_list.add(self)
        self.width = width
        self.height = height
        self.speed = speed
        self.power = power
        self.way = way
        self.image = pg.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = col.WHITE
        self.image.fill(self.color)

    def update(self):
        self.rect.x += self.speed * self.way[0]
        if self.rect.x < 0 or self.rect.x > self.game.config.SIZE[0]:
            self.kill()
            return
        self.rect.y += self.speed * self.way[1]
        if self.rect.y < 0 or self.rect.y > self.game.config.SIZE[1]:
            self.kill()
            return
        if pg.sprite.spritecollide(self, self.game.block_list, False):
            self.kill()
