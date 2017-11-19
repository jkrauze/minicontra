import pygame as pg


class Platform(pg.sprite.Sprite):
    def __init__(self, game, width, height, x, y):
        super().__init__()
        self.game = game
        self.game.block_list.add(self)
        self.game.sprites_list.add(self)
        self.width = width
        self.height = height
        self.image = pg.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = (100, 100, 0)
        self.image.fill(self.color)
