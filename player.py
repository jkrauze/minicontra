import pygame as pg
import config as c
import color as col


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 30
        self.image = pg.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.bottom = c.SIZE[1] - self.height
        self.wall = c.SIZE[0] - self.width
        self.rect.x = c.SIZE[0] // 2
        self.rect.y = self.bottom
        self.v_x = 0
        self.v_y = 0
        self.a_x = 0
        self.a_y = 0
        self.v_max = 5
        self.friction = 0.75
        self.color = col.BLUE
        self.image.fill(self.color)
        self.moving_left = False
        self.moving_right = False
        self.last_move = 0

    def update(self):
        way = 0
        if self.moving_right and self.moving_left:
            way = self.last_move
        elif self.moving_left:
            way = 1
        elif self.moving_right:
            way = 2
        if way == 1:
            if self.rect.y == self.bottom:
                self.a_x = -3
            else:
                self.a_x = -1
        elif way == 2:
            if self.rect.y == self.bottom:
                self.a_x = 3
            else:
                self.a_x = 1
        if self.rect.y < self.bottom:
            self.a_y = 1
        self.v_x += self.a_x
        self.v_y += self.a_y
        if self.rect.y == self.bottom:
            self.v_x *= self.friction
        if self.v_x > self.v_max:
            self.v_x = self.v_max
        elif self.v_x < -self.v_max:
            self.v_x = -self.v_max
        elif abs(self.v_x) < 1:
            self.v_x = 0
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        if self.rect.y > self.bottom:
            self.a_y = 0
            self.v_y = 0
            self.rect.y = self.bottom
        if self.rect.x < 0:
            self.a_x = 0
            self.v_x = 0
            self.rect.x = 0
        elif self.rect.x > self.wall:
            self.a_x = 0
            self.v_x = 0
            self.rect.x = self.wall
        print("x:{};y:{};v_x:{:.2f};v_y:{:.2f};a_x:{};a_y:{}".format(self.rect.x, self.rect.y, self.v_x, self.v_y,
                                                                     self.a_x, self.a_y))

    def jump(self):
        if self.bottom - self.rect.y < 3:
            self.a_y = 0
            self.v_y = -15

    def jump_stop(self):
        if self.v_y < 0:
            self.v_y /= 20

    def move_left(self):
        self.moving_left = True
        self.last_move = 1

    def move_left_stop(self):
        self.moving_left = False
        if self.a_x < 0:
            self.a_x = 0

    def move_right(self):
        self.moving_right = True
        self.last_move = 2

    def move_right_stop(self):
        self.moving_right = False
        if self.a_x > 0:
            self.a_x = 0
