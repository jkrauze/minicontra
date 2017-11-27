import pygame as pg
import random
from image import Image


class Rock(Image):
    _sprite_positions = [(0, 1), (0, 7), (0, 14), (0, 16), (0, 21), (0, 28), (1, 4), (1, 5), (1, 6), (1, 7), (1, 10),
                         (1, 20), (1, 23), (1, 24), (1, 26), (1, 27)]

    def __init__(self, game, x, y):
        self.sprite_pos = self._sprite_positions[random.randint(0, len(self._sprite_positions) - 1)]
        image = game.ground_sprite.subsurface((160 * self.sprite_pos[0], 32 * self.sprite_pos[1], 32, 32))
        super().__init__(game, image, x, y)
