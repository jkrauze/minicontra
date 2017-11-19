import pygame as pg
import config as c
import color as col
from bullet import Bullet
from block import Block
from platform import Platform


class Player(pg.sprite.Sprite):
    def __init__(self, game, number):
        super().__init__()
        self.game = game
        self.game.sprites_list.add(self)
        self.number = number
        self.width = 20
        self.height = 30
        self.hp = 3
        self.image = pg.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.screen_middle = self.game.config.SIZE[0] // 2
        self.rect.x = self.game.config.SIZE[0] // 2
        self.rect.y = self.game.config.SIZE[1] - 200
        self.v = [0, 0]
        self.a = [0, 0]
        self.v_max = 4
        self.friction = 0.51
        self.shooting_frequency = 10
        self.color = col.GREEN
        self.image.fill(self.color)
        self.moving_left = False
        self.moving_right = False
        self.looking_up = False
        self.looking_down = False
        self.shooting = -1
        self.recovering = 0
        self.last_move = 1
        self.last_look = 0

    def direction_x(self):
        way = 0
        if self.moving_right and self.moving_left:
            way = self.last_move
        elif self.moving_left:
            way = -1
        elif self.moving_right:
            way = 1
        return way

    def direction_y(self):
        way = 0
        if self.looking_up and self.looking_down:
            way = self.last_look
        elif self.looking_up:
            way = -1
        elif self.looking_down:
            way = 1
        return way

    def shoot_direction(self):
        x = self.direction_x()
        y = self.direction_y()
        if x == 0 and y == 0:
            x = self.last_move
        return x, y

    def update(self):
        way = self.direction_x()
        self.rect.y += 1
        collides = pg.sprite.spritecollide(self, self.game.block_list, False)
        self.rect.y -= 1
        going_through = pg.sprite.spritecollide(self, self.game.block_list, False)
        if way == 0:
            if collides and not going_through:
                self.a[0] = round(self.v[0] * -self.friction)
            else:
                self.a[0] = 0
        elif way == -1:
            if collides and not going_through:
                self.a[0] = -3
            else:
                self.a[0] = -1
        elif way == 1:
            if collides and not going_through:
                self.a[0] = 3
            else:
                self.a[0] = 1

        if not collides or going_through:
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
        if collides_x and isinstance(collides_x[0], Block):
            if self.v[0] > 0:
                self.rect.right = collides_x[0].rect.left
            else:
                self.rect.left = collides_x[0].rect.right
            self.v[0] = 0
            self.a[0] = 0
        self.rect.y += self.v[1]
        collides_y = pg.sprite.spritecollide(self, self.game.block_list, False)
        if collides_y:
            if self.v[1] > 0 and (not going_through or collides_y[0] not in going_through) and collides_y[0] not in collides_x:
                self.rect.y = collides_y[0].rect.top - self.height
                self.v[1] = 0
                self.a[1] = 0
            elif isinstance(collides_y[0], Block):
                self.rect.y = collides_y[0].rect.bottom
                self.v[1] = 0
                self.a[1] = 0
        if self.rect.y > self.game.config.SIZE[1]:
            self.game.actual_level.done = True
            self.kill()
            return
        if self.rect.x < 0:
            self.a[0] = 0
            self.v[0] = 0
            self.rect.x = 0
        elif self.rect.x > self.screen_middle:
            for block in self.game.sprites_list:
                block.rect.x -= self.v[0]
                if block.rect.right < -self.game.config.SIZE[1] // 2:
                    block.kill()
        if self.shooting > 0:
            self.shooting -= 1
        elif self.shooting == 0:
            self.shooting = self.shooting_frequency
            self.game.player_bullets_list.add(
                Bullet(self.game, 10, 10, 10, 1, self.rect.centerx - 5, self.rect.centery - 5, self.shoot_direction()))
        elif self.shooting < -1:
            self.shooting += 1
        if self.recovering > 0:
            self.recovering -= 1
            self.image.set_alpha(125)
        else:
            self.image.set_alpha(255)

    def hurt(self, hp):
        if self.recovering > 0:
            return
        self.hp = max(self.hp - hp, 0)
        self.recovering = 180
        if self.hp == 0:
            self.game.actual_level.done = True
            self.kill()

    def jump(self):
        x_diff = -self.v[0] * self.game.config.JUMP_PRECISION
        self.rect.x += x_diff
        self.rect.y += 1
        if pg.sprite.spritecollide(self, self.game.block_list, False):
            self.a[1] = 0
            self.v[1] = -15
        self.rect.x -= x_diff
        self.rect.y -= 1

    def jump_stop(self):
        if self.v[1] < 0:
            self.v[1] /= 20

    def move_left(self):
        self.moving_left = True
        self.last_move = -1

    def move_left_stop(self):
        self.moving_left = False
        if self.a[0] < 0:
            self.a[0] = 0

    def move_right(self):
        self.moving_right = True
        self.last_move = 1

    def move_right_stop(self):
        self.moving_right = False
        if self.a[0] > 0:
            self.a[0] = 0

    def look_up(self):
        self.looking_up = True
        self.last_look = -1

    def look_up_stop(self):
        self.looking_up = False

    def look_down(self):
        self.looking_down = True
        self.last_look = 1

    def look_down_stop(self):
        self.looking_down = False

    def shoot(self):
        if self.shooting == -1:
            self.shooting = 0

    def shoot_stop(self):
        if self.shooting > 0:
            self.shooting = -self.shooting
        elif self.shooting == 0:
            self.shooting = -1

    def stop(self):
        self.shooting = -1
        self.moving_right = False
        self.moving_left = False
        self.looking_up = False
        self.looking_down = False
        self.a[0] = 0

    def handle_keydown(self, key):
        if key == self.game.config.KEY_LEFT[self.number]:
            self.move_left()
        elif key == self.game.config.KEY_RIGHT[self.number]:
            self.move_right()
        elif key == self.game.config.KEY_DOWN[self.number]:
            self.look_down()
        elif key == self.game.config.KEY_UP[self.number]:
            self.look_up()
        elif key == self.game.config.KEY_JUMP[self.number]:
            self.jump()
        elif key == self.game.config.KEY_SHOOT[self.number]:
            self.shoot()

    def handle_keyup(self, key):
        if key == self.game.config.KEY_LEFT[self.number]:
            self.move_left_stop()
        elif key == self.game.config.KEY_RIGHT[self.number]:
            self.move_right_stop()
        elif key == self.game.config.KEY_DOWN[self.number]:
            self.look_down_stop()
        elif key == self.game.config.KEY_UP[self.number]:
            self.look_up_stop()
        elif key == self.game.config.KEY_JUMP[self.number]:
            self.jump_stop()
        elif key == self.game.config.KEY_SHOOT[self.number]:
            self.shoot_stop()
