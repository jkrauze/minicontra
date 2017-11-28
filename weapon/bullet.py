import pygame as pg
import config as c
import color as col
from block import Block


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, speed, power, center_x, center_y, way):
        super().__init__()
        self.game = game
        self.game.player_bullets_list.add(self)
        self.game.sprites_list.add(self)
        self.speed = speed
        self.power = power
        self.way = way
        self.image = self.set_image()
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.mask = pg.mask.from_surface(self.image)

    def set_image(self):
        raise NotImplementedError('set_image method must be implemented by bullet subclass')

    def update(self):
        self.rect.x += self.speed * self.way[0]
        if self.rect.x < 0 or self.rect.x > self.game.config.SIZE[0]:
            self.kill()
            return
        self.rect.y += self.speed * self.way[1]
        if self.rect.y < 0 or self.rect.y > self.game.config.SIZE[1]:
            self.kill()
            return
        collides = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        if collides and isinstance(collides[0], Block):
            self.kill()
