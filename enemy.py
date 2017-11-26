import pygame as pg
import config as c
import color as col


class Enemy(pg.sprite.Sprite):
    def __init__(self, game, hp, x, y):
        super().__init__()
        self.game = game
        self.game.enemies_list.add(self)
        self.game.sprites_list.add(self)
        self.hp = hp
        self.width = 50
        self.height = 50
        self.image = pg.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.bottom = self.game.config.SIZE[1] - self.height
        self.middle = self.game.config.SIZE[0] // 2
        self.rect.x = x
        self.rect.y = y
        self.v = [0, 0]
        self.a = [0, 0]
        self.v_max = 2
        self.friction = 0.51
        self.shooting_frequency = 10
        self.color = col.RED
        self.image.fill(self.color)
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
            self.image = self.game.enemy_sprite.subsurface((24 + 51 * (self.run_animation // 3), 286, 50, 50))
        else:
            self.image = self.game.enemy_sprite.subsurface((24 + 51 * (self.run_animation // 3), 346, 50, 50))
        self.run_animation = (self.run_animation + 1) % 24

    def update(self):
        self.rect.y += 1
        collides = pg.sprite.spritecollide(self, self.game.block_list, False)
        self.rect.y -= 1
        if self.v == [0, 0]:
            self.moving_right, self.moving_left = self.moving_left, self.moving_right
        way = self.direction_x()
        if way == 0 and collides:
            self.a[0] = round(self.v[0] * -self.friction)
        elif way == -1:
            if collides:
                self.a[0] = -3
            else:
                self.a[0] = 0
        elif way == 1:
            if collides:
                self.a[0] = 3
            else:
                self.a[0] = 0

        if not collides:
            self.a[1] = 1
        else:
            self.a[1] = 0
            if self.v[1] > 0:
                self.rect.y = collides[0].rect.top - self.height
                self.v[1] = 0

        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
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
        self.rect.y += self.v[1]
        collides_y = pg.sprite.spritecollide(self, self.game.block_list, False)
        if collides_y:
            if self.v[1] > 0:
                self.rect.y = collides_y[0].rect.top - self.height
            else:
                self.rect.y = collides_y[0].rect.bottom
            self.v[1] = 0
            self.a[1] = 0

        if collides:
            way = self.direction_x()
            self.rect.x += way
            self.rect.y += 1
            collides = pg.sprite.spritecollide(self, self.game.block_list, False)
            self.rect.y -= 1
            self.rect.x -= way
            if len(collides) == 1:
                floor = (collides[0].rect.left, collides[0].rect.right)
                if self.rect.x <= floor[0]:
                    self.rect.x = floor[0]
                    self.v = [-1, 0]
                    self.a = [0, 0]
                    self.moving_right, self.moving_left = True, False
                elif self.rect.x >= floor[1] - self.width:
                    self.rect.x = floor[1] - self.width
                    self.v = [1, 0]
                    self.a = [0, 0]
                    self.moving_right, self.moving_left = False, True

        self.set_image()
