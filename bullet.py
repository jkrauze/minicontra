import pygame as pg
import config as c
import color as col
from block import Block


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, width, height, speed, power, center_x, center_y, way):
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
        self.rect.centerx = center_x
        self.rect.centery = center_y

    def set_image(self):
        if self.way[0] == 0:
            if self.way[1] == -1:
                self.image = self.game.bullet_sprite.subsurface((424, 13, 15, 15))
            else:
                self.image = self.game.bullet_sprite.subsurface((424, 60, 15, 15))
        elif self.way[0] == 1:
            if self.way[1] == 0:
                self.image = self.game.bullet_sprite.subsurface((448, 37, 15, 15))
            elif self.way[1] == -1:
                self.image = self.game.bullet_sprite.subsurface((448, 12, 15, 15))
            else:
                self.image = self.game.bullet_sprite.subsurface((448, 61, 15, 15))
        else:
            if self.way[1] == 0:
                self.image = self.game.bullet_sprite.subsurface((399, 37, 15, 15))
            elif self.way[1] == -1:
                self.image = self.game.bullet_sprite.subsurface((399, 12, 15, 15))
            else:
                self.image = self.game.bullet_sprite.subsurface((399, 61, 15, 15))

    def update(self):
        self.rect.x += self.speed * self.way[0]
        if self.rect.x < 0 or self.rect.x > self.game.config.SIZE[0]:
            self.kill()
            return
        self.rect.y += self.speed * self.way[1]
        if self.rect.y < 0 or self.rect.y > self.game.config.SIZE[1]:
            self.kill()
            return
        collides = pg.sprite.spritecollide(self, self.game.block_list, False)
        if collides and isinstance(collides[0], Block):
            self.kill()
        self.set_image()
