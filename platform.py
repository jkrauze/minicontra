import pygame as pg
import random
from image import Image
from rock import Rock


class Platform(pg.sprite.Sprite):
    _sprite_positions = [(0, 2), (0, 24), (0, 26), (1, 18), (1, 29), (2, 2), (2, 7), (2, 17)]

    def __init__(self, game, width, height, x, y):
        super().__init__()
        self.game = game
        self.game.block_list.add(self)
        self.game.sprites_list.add(self)
        self.width = width
        self.height = height
        self.sprite_pos = self._sprite_positions[random.randint(0, len(self._sprite_positions) - 1)]
        self.image = self.game.ground_sprite.subsurface(
            (32 + 160 * self.sprite_pos[0], 32 * self.sprite_pos[1], 32, 32))
        self.image = pg.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rock = Rock(self.game, x, y)
        self.over_image = Image(self.game,
                                self.game.ground_sprite.subsurface(
                                    (64 + 160 * self.sprite_pos[0], 32 * self.sprite_pos[1], 32, 32)), x,
                                y - 20)
