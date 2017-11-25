import pygame as pg


class Image(pg.sprite.Sprite):
    def __init__(self, game, image, x, y):
        super().__init__()
        self.game = game
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game.sprites_list.add(self)
