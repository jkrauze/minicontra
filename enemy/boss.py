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

    def update(self):
        if self.rect.x > self.game.config.SIZE[0]:
            return
        way = self.direction_x()
        diff = max(1, self.v[1])
        self.rect.y += diff
        standing = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
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
        collides_y = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
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
            collides = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
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
        self.weapon.handle_shooting(self.rect.centerx - 50,
                                    self.rect.centery,
                                    (way, 0))
