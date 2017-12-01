import pygame as pg
from weapon.boss_weapon import BossWeapon


class Boss(pg.sprite.Sprite):
    def __init__(self, game, hp, x, y):
        super().__init__()
        self.game = game
        self.game.enemies_list.add(self)
        self.game.sprites_list.add(self)
        self.hp = hp
        self.width = 140
        self.height = 108
        self.image = self.game.boss_sprite.subsurface((136, 155, 140, 108))
        self.rect = self.image.get_rect()
        self.bottom = self.game.config.SIZE[1] - self.height
        self.middle = self.game.config.SIZE[0] // 2
        self.rect.x = x
        self.rect.y = y
        self.v = [0, 0]
        self.a = [0, 0]
        self.v_max = 2
        self.mask = pg.mask.from_surface(self.image)
        self.weapon = BossWeapon(game)
        self.moving_left = True
        self.moving_right = False

    def direction_x(self):
        way = 0
        if self.moving_left:
            way = -1
        elif self.moving_right:
            way = 1
        return way

    def set_image(self):
        if self.weapon.state == self.weapon.shooting_frequency-10:
            self.image = self.game.boss_sprite.subsurface((136, 155, 140, 108))
        elif self.weapon.state>20:
            return
        elif self.weapon.state>5:
            self.image = self.game.boss_sprite.subsurface((136, 267, 140, 108))
        else:
            self.image = self.game.boss_sprite.subsurface((277, 267, 140, 108))



    def update(self):
        if self.rect.x > self.game.config.SIZE[0]:
            return
        way = self.direction_x()
        diff = max(1, self.v[1])
        self.rect.y += diff
        standing = pg.sprite.spritecollide(self, self.game.block_list, False)
        self.on_ground = bool(standing)
        self.rect.y -= diff
        way = self.direction_x()

        if not standing:
            self.a[1] = 1
        else:
            self.a[1] = 0
            if self.v[1] > 0:
                self.rect.y = standing[0].rect.top - self.height
                self.v[1] = 0

        self.v[1] += self.a[1]

        self.rect.y += self.v[1]
        collides_y = pg.sprite.spritecollide(self, self.game.block_list, False)
        if collides_y:
            if self.v[1] > 0:
                self.rect.y = collides_y[0].rect.top - self.height
            else:
                self.rect.y = collides_y[0].rect.bottom
            self.v[1] = 0
            self.a[1] = 0

        if standing:
            way = self.direction_x()
            self.rect.x += way * 30
            self.rect.y += 1
            collides = pg.sprite.spritecollide(self, self.game.block_list, False)
            self.rect.y -= 1
            self.rect.x -= way * 30
            if len(collides) == 0:
                floor = (standing[0].rect.left, standing[0].rect.right)
                if self.rect.x <= floor[0]:
                    self.v = [-1, 0]
                    self.a = [0, 0]
                    self.moving_right, self.moving_left = True, False
                elif self.rect.x >= floor[1] - self.width:
                    self.v = [1, 0]
                    self.a = [0, 0]
                    self.moving_right, self.moving_left = False, True
        self.weapon.handle_shooting(self.rect.left + 15,
                                    self.rect.centery - 10,
                                    (way, 0))
        self.set_image()