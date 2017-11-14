import pygame as pg
import config as c
import color as col


class Player():
    def __init__(self):
        self.width = 10
        self.height = 30
        self.bottom = c.SIZE[1] - self.height
        self.wall = c.SIZE[0] - self.width
        self.x = c.SIZE[0] // 2
        self.y = self.bottom
        self.v_x = 0
        self.v_y = 0
        self.a_x = 0
        self.a_y = 0
        self.v_max = 5
        self.friction = 0.5

    def update(self):
        if self.y < self.bottom:
            self.a_y += 0.15
        self.v_x += self.a_x
        self.v_y += self.a_y
        if self.y == self.bottom:
            self.v_x *= self.friction
        if self.v_x > self.v_max:
            self.v_x = self.v_max
        elif self.v_x < -self.v_max:
            self.v_x = -self.v_max
        self.x += self.v_x
        self.y += self.v_y
        if self.y > self.bottom:
            self.a_y = 0
            self.v_y = 0
            self.y = self.bottom
        if self.x < 0:
            self.a_x = 0
            self.v_x = 0
            self.x = 0
        elif self.x > self.wall:
            self.a_x = 0
            self.v_x = 0
            self.x = self.wall

    def draw(self, screen):
        pg.draw.rect(screen, col.GREEN, [self.x, self.y, self.width, self.height])

    def jump(self):
        if self.bottom - self.y < 3:
            self.a_y = 0
            self.v_y = -15

    def jump_stop(self):
        if self.v_y < 0:
            self.v_y /= 20

    def move_left(self):
        self.a_x = -3

    def move_left_stop(self):
        if self.a_x < 0:
            self.a_x = 0

    def move_right(self):
        self.a_x = 3

    def move_right_stop(self):
        if self.a_x > 0:
            self.a_x = 0
