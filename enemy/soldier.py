import pygame as pg
from weapon.soldier_weapon import SoldierWeapon


class Soldier(pg.sprite.Sprite):
    def __init__(self, game, hp, x, y):
        super().__init__()
        self.game = game
        self.visible = False if x > 640 else True
        if self.visible:
            self.game.enemies_list.add(self)
        self.game.sprites_list.add(self)
        self.hp = hp
        self.width = 50
        self.height = 50
        self.image = self.game.enemy_subsprites[0][0]
        self.rect = self.image.get_rect()
        self.bottom = self.game.config.SIZE[1] - self.height
        self.middle = self.game.config.SIZE[0] // 2
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.game.enemy_subsprites[2])
        self.v = [-1, 0]
        self.a = [-1, 0]
        self.v_max = 2
        self.friction = 0.51
        self.shooting_frequency = 30
        self.weapon = SoldierWeapon(game)
        self.moving_left = True
        self.moving_right = False
        self.run_animation = 0

    def direction_x(self):
        way = 0
        if self.moving_left:
            way = -1
        elif self.moving_right:
            way = 1
        return way

    def set_image(self):
        if self.direction_x() == 1:
            self.image = self.game.enemy_subsprites[0][self.run_animation // 3]
        else:
            self.image = self.game.enemy_subsprites[1][self.run_animation // 3]
        self.run_animation = (self.run_animation + 1) % 24

    def update(self):
        if not self.visible:
            if self.rect.x < 640:
                self.game.enemies_list.add(self)
                self.visible = True
            else:
                return
        way = self.direction_x()
        diff = max(1, self.v[1])
        self.rect.y += diff
        standing = pg.sprite.spritecollide(self, self.game.block_list, False)
        if not standing:
            self.kill()
            return
        self.rect.y -= diff
        if self.v == [0, 0]:
            self.moving_right, self.moving_left = self.moving_left, self.moving_right
        way = self.direction_x()
        self.a[0] = 3 * way
        if self.v[1] > 0:
            self.rect.y = standing[0].rect.top - self.height
            self.v[1] = 0

        self.v[0] += self.a[0]
        if self.v[0] > self.v_max:
            self.v[0] = self.v_max
        elif self.v[0] < -self.v_max:
            self.v[0] = -self.v_max

        self.rect.x += self.v[0]
        collides_x = pg.sprite.spritecollide(self, self.game.block_list, False)
        if collides_x:
            if self.v[0] > 0:
                self.rect.right = collides_x[0].rect.left
            else:
                self.rect.left = collides_x[0].rect.right
            self.v[0] = 0
            self.a[0] = 0

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
        self.weapon.handle_shooting(self.rect.centerx - 6 * way,
                                    self.rect.centery - 6,
                                    (way, 0))
        self.set_image()
