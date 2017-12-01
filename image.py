import pygame as pg


class Image(pg.sprite.Sprite):
    def __init__(self, game, image, x, y):
        super().__init__()
        self.game = game
        self.visible = False if x > 700 else True
        if self.visible:
            self.game.background_list.add(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game.sprites_list.add(self)

    def update(self):
        if not self.visible:
            if self.rect.x < 700:
                self.game.background_list.add(self)
                self.visible = True
