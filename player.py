import pygame as pg
import weapon.default_weapon
from block import Block
from platform import Platform


class Player(pg.sprite.Sprite):
    def __init__(self, game, number, x, y):
        super().__init__()
        self.game = game
        self.game.sprites_list.add(self)
        self.game.players_list.add(self)
        self.number = number
        self.width = 50
        self.height = 50
        self.hp = 3
        self.image = self.game.player_sprite.subsurface((24, 143, 50, 50))
        self.rect = self.image.get_rect()
        self.screen_middle = self.game.config.SIZE[0] // 2
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.game.enemy_sprite.subsurface((24, 186, 50, 50)))
        self.v = [0, 0]
        self.a = [0, 0]
        self.v_max = 4
        self.friction = 0.51
        self.shooting_frequency = 10
        self.moving_left = False
        self.moving_right = False
        self.looking_up = False
        self.looking_down = False
        self.weapon = weapon.default_weapon.DefaultWeapon(self.game)
        self.recovering = 0
        self.last_move = 1
        self.last_look = 0
        self.run_animation = 0
        self.on_ground = False

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

    def set_image(self):
        actual_midbottom = self.rect.midbottom
        x_move = self.direction_x()
        y_move = self.direction_y()
        if not self.on_ground:
            if x_move == 0 and y_move != 0:
                if self.last_move == 1:
                    if y_move == -1:
                        self.image = self.game.player_sprite.subsurface((137, 683, 50, 50))
                    else:
                        self.image = self.game.player_sprite.subsurface((137, 746, 50, 50))
                else:
                    if y_move == -1:
                        self.image = self.game.player_sprite.subsurface((193, 683, 50, 50))
                    else:
                        self.image = self.game.player_sprite.subsurface((193, 746, 50, 50))
            elif x_move == 1 or self.last_move == 1:
                if y_move == 0:
                    self.image = self.game.player_sprite.subsurface((126, 143, 50, 50))
                elif y_move == -1:
                    self.image = self.game.player_sprite.subsurface((331, 925, 50, 50))
                else:
                    self.image = self.game.player_sprite.subsurface((760, 925, 50, 50))
            else:
                if y_move == 0:
                    self.image = self.game.player_sprite.subsurface((126, 200, 50, 50))
                elif y_move == -1:
                    self.image = self.game.player_sprite.subsurface((331, 1063, 50, 50))
                else:
                    self.image = self.game.player_sprite.subsurface((760, 1063, 50, 50))
            self.run_animation = 0
        elif x_move == 0:
            if self.last_move == 1:
                if y_move == 0:
                    self.image = self.game.player_sprite.subsurface((24, 143, 50, 50))
                elif y_move == -1:
                    self.image = self.game.player_sprite.subsurface((137, 683, 50, 50))
                else:
                    self.image = self.game.player_sprite.subsurface((137, 746, 50, 50))
            else:
                if y_move == 0:
                    self.image = self.game.player_sprite.subsurface((24, 200, 50, 50))
                elif y_move == -1:
                    self.image = self.game.player_sprite.subsurface((193, 683, 50, 50))
                else:
                    self.image = self.game.player_sprite.subsurface((193, 746, 50, 50))
            self.run_animation = 0
        else:
            if x_move == 1:
                if y_move == 0:
                    self.image = self.game.player_sprite.subsurface((24 + 51 * (self.run_animation // 3), 315, 50, 50))
                elif y_move == -1:
                    self.image = self.game.player_sprite.subsurface((25 + 51 * (self.run_animation // 3), 932, 50, 50))
                else:
                    self.image = self.game.player_sprite.subsurface((454 + 51 * (self.run_animation // 3), 932, 50, 50))
            else:
                if y_move == 0:
                    self.image = self.game.player_sprite.subsurface((24 + 51 * (self.run_animation // 3), 375, 50, 50))
                elif y_move == -1:
                    self.image = self.game.player_sprite.subsurface((25 + 51 * (self.run_animation // 3), 1070, 50, 50))
                else:
                    self.image = self.game.player_sprite.subsurface(
                        (454 + 51 * (self.run_animation // 3), 1070, 50, 50))
            self.run_animation = (self.run_animation + 1) % 24
        self.rect = self.image.get_rect()
        self.rect.midbottom = actual_midbottom

    def update(self):
        way = self.direction_x()
        diff = max(1, self.v[1])
        self.rect.y += diff
        standing = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        self.on_ground = bool(standing)
        self.rect.y -= diff
        going_through = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        for elem in going_through:
            try:
                standing.remove(elem)
            except ValueError:
                pass
        if way == 0:
            if standing:
                self.a[0] = round(self.v[0] * -self.friction)
            else:
                self.a[0] = 0
        elif way == -1:
            if standing:
                self.a[0] = -3
            else:
                self.a[0] = -1
        elif way == 1:
            if standing:
                self.a[0] = 3
            else:
                self.a[0] = 1

        if not standing:
            self.a[1] = 0.75
        else:
            self.a[1] = 0
            if self.v[1] > 0:
                self.rect.y = standing[0].rect.top - self.height
                self.v[1] = 0

        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        if self.v[0] > self.v_max:
            self.v[0] = self.v_max
        elif self.v[0] < -self.v_max:
            self.v[0] = -self.v_max

        self.rect.x += self.v[0]
        collides_x = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        if collides_x and isinstance(collides_x[0], Block):
            if self.v[0] > 0:
                self.rect.right = collides_x[0].rect.left
            else:
                self.rect.left = collides_x[0].rect.right
            self.v[0] = 0
            self.a[0] = 0
        self.rect.y += self.v[1]
        collides_y = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        if collides_y:
            if self.v[1] > 0 and (not going_through or collides_y[0] not in going_through) and collides_y[
                0] not in collides_x:
                self.rect.y = collides_y[0].rect.top - self.height
                self.v[1] = 0
                self.a[1] = 0
            elif isinstance(collides_y[0], Block):
                self.rect.y = collides_y[0].rect.bottom
                self.v[1] = 0
                self.a[1] = 0
        if self.rect.y > self.game.config.SIZE[1]:
            self.game.actual_level.players_alive -= 1
            self.hp = 0
            self.kill()
            return
        if self.rect.x < 0:
            self.a[0] = 0
            self.v[0] = 0
            self.rect.x = 0
        elif self.rect.x > self.game.actual_level.level_border:
            self.a[0] = 0
            self.v[0] = 0
            self.rect.x = self.game.actual_level.level_border
        elif self.rect.x > self.screen_middle:
            self.game.actual_level.actual_length += self.v[0]
            self.game.actual_level.level_border -= self.v[0]
            for block in self.game.sprites_list:
                block.rect.x -= self.v[0]
                if block.rect.right < -self.game.config.SIZE[1] // 2:
                    block.kill()
        self.weapon.handle_shooting(self.rect.centerx - 6 * self.last_move,
                                    self.rect.centery - 6 - 8 * self.direction_y(),
                                    self.shoot_direction())
        self.set_image()
        if self.recovering > 0:
            self.recovering -= 1
            self.image.set_alpha(100)
        else:
            self.image.set_alpha(255)

    def hurt(self, hp):
        if self.recovering > 0:
            return
        self.game.hit_sound.play()
        self.hp = max(self.hp - hp, 0)
        self.recovering = 180
        if self.hp == 0:
            self.game.actual_level.players_alive -= 1
            self.kill()

    def jump(self):
        collides = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        x_diff = -self.v[0] * self.game.config.JUMP_PRECISION
        self.rect.x += x_diff
        self.rect.y += 1
        standing_on = pg.sprite.spritecollide(self, self.game.block_list, False, pg.sprite.collide_mask)
        for elem in collides:
            try:
                standing_on.remove(elem)
            except ValueError:
                pass
        if standing_on:
            if self.looking_down and isinstance(standing_on[0], Platform):
                self.rect.y += 1
            else:
                self.a[1] = 0
                self.v[1] = -12
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
        self.weapon.start_shooting()

    def shoot_stop(self):
        self.weapon.stop_shooting()

    def stop(self):
        self.weapon.stop_shooting()
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
