import pygame as pg
from image import Image


class Block(pg.sprite.Sprite):
    def __init__(self, game, width, height, x, y):
        super().__init__()
        self.game = game
        self.game.block_list.add(self)
        self.game.sprites_list.add(self)
        self.width = width
        self.height = height
        self.image = self.game.ground_sprite.subsurface((0, 6 * 32, 32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.over_image = Image(self.game, self.game.ground_sprite.subsurface((2 * 32, 6 * 32, 32, 32)), x, y - 32)
