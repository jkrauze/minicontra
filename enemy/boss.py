import pygame as pg
from weapon.boss_weapon import BossWeapon


class Boss(pg.sprite.Sprite):
    def __init__(self, game, hp, x, y):
        super().__init__()
        self.game = game
        self.visible = False if x > 640 else True
        if self.visible:
            self.game.enemies_list.add(self)
        self.game.sprites_list.add(self)
        self.hp = hp
        self.width = 140
        self.height = 108
        self.image = self.game.boss_sprite.subsurface((136, 155, 140, 108))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.weapon = BossWeapon(game)

    def set_image(self):
        if self.weapon.state == self.weapon.shooting_frequency - 10:
            self.image = self.game.boss_subsprites[0]
        elif self.weapon.state > 20:
            return
        elif self.weapon.state > 5:
            self.image = self.game.boss_subsprites[1]
        else:
            self.image = self.game.boss_subsprites[2]

    def update(self):
        if not self.visible:
            if self.rect.x < 640:
                self.game.enemies_list.add(self)
                self.visible = True
            else:
                return
        self.weapon.handle_shooting(self.rect.left + 15,
                                    self.rect.centery - 10,
                                    (-1, 0))
        self.set_image()
