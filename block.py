import pygame as pg
import random
from image import Image


class Block(pg.sprite.Sprite):
    _sprite_positions = [(0, 0), (0, 3), (0, 5), (0, 9), (0, 10), (0, 22), (0, 23), (0, 27), (0, 31), (1, 3), (1, 8),
                         (1, 9), (1, 11), (1, 13), (1, 15), (1, 16), (1, 28)]

    def __init__(self, game, width, height, x, y):
        super().__init__()
        self.game = game
        self.game.block_list.add(self)
        self.game.sprites_list.add(self)
        self.width = width
        self.height = height
        self.sprite_pos = self._sprite_positions[random.randint(0, len(self._sprite_positions) - 1)]
        self.image = self.game.ground_sprite.subsurface((160 * self.sprite_pos[0], 32 * self.sprite_pos[1], 32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.over_image = Image(self.game,
                                self.game.ground_sprite.subsurface(
                                    (64 + 160 * self.sprite_pos[0], 32 * self.sprite_pos[1], 32, 32)), x,
                                y - 20)
