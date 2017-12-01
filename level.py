import pygame as pg
import os
import time
import math
import color as col
from config import Config
from block import Block
from platform import Platform
from enemy.soldier import Soldier
from player import Player
from menu import Menu
from rock import Rock
from enemy.boss import Boss


class Level:
    def __init__(self, game, file_path, player_count):
        self.game = game
        self.highscore_file_path = file_path[:4] + "." + file_path[4:] + ".score"
        if not os.path.isfile(self.highscore_file_path):
            with open(self.highscore_file_path, 'w') as file:
                file.write('0')
        with open(self.highscore_file_path, 'r') as file:
            self.highscore = int(file.read())
        self.score = 0
        self.name = file_path[4:-4]
        self.file_path = file_path
        self.length = 0
        self.success = False
        self.player_count = player_count
        self.player = None
        self.player2 = None
        self.boss = None

        def check_border(line, line_len, pos):
            border = 0
            if pos > 0 and line[pos - 1] == ' ':
                border = -1
            elif pos < line_len - 1 and line[pos + 1] == ' ':
                border = 1
            return border

        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 0):
                line_len = len(line)
                if len(line) > self.length:
                    self.length = line_len
                for pos, char in enumerate(line, 0):
                    if char == 'b':
                        Block(self.game, 32, 32, 32 * pos, 32 * line_num)
                    elif char == 'p':
                        Platform(self.game, 32, 32, 32 * pos, 32 * line_num, check_border(line, line_len, pos))
                    elif char == 's':
                        Soldier(self.game, 1, 32 * pos, 32 * line_num - 28)
                    elif char == 'x':
                        self.player = Player(self.game, 0, 32 * pos, 32 * line_num - 28)
                        if self.player_count == 2:
                            self.player2 = Player(self.game, 1, 32 * pos, 32 * line_num - 28)
                    elif char == 'f':
                        self.boss = Boss(self.game, 15, 32 * pos, 32 * line_num - 76)
                        self.level_border = 32 * pos + 16
                    if char == 'l' or (char != ' ' and pos > 0 and line[pos - 1] == 'l' and pos < line_len - 1 and line[
                            pos + 1] == 'l'):
                        Rock(self.game, 32 * pos, 32 * line_num, check_border(line, line_len, pos))
        if not self.player:
            raise Exception("No player in {} level!".format(file))
        if not self.boss:
            raise Exception("No boss in {} level!".format(file))
        self.length *= 32
        self.actual_length = self.player.rect.x
        self.players_alive = player_count
        self.return_state = 0
        self.clock = pg.time.Clock()
        self.player_health = [pg.image.load(os.path.join('img', 'heart.png')).convert(),
                              pg.image.load(os.path.join('img', 'heart.png')).convert(),
                              pg.image.load(os.path.join('img', 'heart.png')).convert()]
        for elem in self.player_health:
            elem.set_colorkey(col.BLACK)
        self.player2_health = [pg.image.load(os.path.join('img', 'heart.png')).convert(),
                               pg.image.load(os.path.join('img', 'heart.png')).convert(),
                               pg.image.load(os.path.join('img', 'heart.png')).convert()]
        for elem in self.player2_health:
            elem.set_colorkey(col.BLACK)

    def draw_start_card(self):
        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        self.game.screen.blit(
            pg.font.Font(self.game.font, 40).render("level " + self.name, 1, self.game.font_color), (50, 50))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render("game score", 1, self.game.font_color_not_active), (50, 200))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render("level highscore", 1, self.game.font_color_not_active), (50, 250))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render("game highscore", 1, self.game.font_color_not_active), (50, 300))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render(str(self.game.score), 1, self.game.font_color_not_active), (350, 200))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render(str(self.highscore), 1, self.game.font_color_not_active), (350, 250))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render(str(self.game.highscore), 1, self.game.font_color_not_active), (350, 300))
        self.game.screen_draw()

    def run(self):
        self.draw_start_card()
        time.sleep(2)
        self.draw_screen()
        self.game.screen_fadein()
        pg.mixer.music.load(os.path.join('snd', 'game.ogg'))
        pg.mixer.music.set_volume(0.7)
        pg.mixer.music.play(-1)
        pg.event.clear()
        while self.players_alive > 0:
            self.tick()
        pg.mixer.music.stop()
        if self.success:
            self.game.score += self.score
            if self.score > self.highscore:
                with open(self.highscore_file_path, 'w') as file:
                    file.write(str(self.score))
            self.draw_screen()
            self.draw_hud()
            self.game.screen_draw()
            time.sleep(0.5)
            self.game.win_sound.play()
            time.sleep(3)
            self.game.screen_fadeout()
        self.game.background_list.empty()
        self.game.block_list.empty()
        self.game.player_bullets_list.empty()
        self.game.enemy_bullets_list.empty()
        self.game.enemies_list.empty()
        self.game.sprites_list.empty()
        self.game.players_list.empty()
        return self.return_state

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.players_alive = 0
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    while self.players_alive > 0:
                        pg.mixer.music.pause()
                        option = Menu(self.game, "Paused", ["Resume", "Restart", "Return to menu", "Exit game"],
                                      0).run()
                        if option == 0:
                            self.player.stop()
                            if self.player_count == 2:
                                self.player2.stop()
                            pg.mixer.music.unpause()
                            break
                        self.players_alive = 0
                        self.return_state = option
                        return
                else:
                    self.player.handle_keydown(event.key)
                    if self.player_count == 2:
                        self.player2.handle_keydown(event.key)
            elif event.type == pg.KEYUP:
                self.player.handle_keyup(event.key)
                if self.player_count == 2:
                    self.player2.handle_keyup(event.key)

    def draw_screen(self):
        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        background_rect = pg.Rect((0, 0), Config.SIZE)
        background_rect.y = -100
        background_rect.x = round(-(1280 - Config.SIZE[0]) * (self.actual_length / self.length))
        self.game.screen.blit(self.game.background, background_rect)
        self.game.sprites_list.update()
        self.game.background_list.draw(self.game.screen)
        self.game.block_list.draw(self.game.screen)
        self.game.player_bullets_list.draw(self.game.screen)
        self.game.enemy_bullets_list.draw(self.game.screen)
        self.game.enemies_list.draw(self.game.screen)
        self.game.players_list.draw(self.game.screen)

    def tick(self):
        self.handle_events()
        if self.players_alive == 0:
            return
        self.draw_screen()
        self.handle_enemy_touch()
        self.handle_shooting()
        self.draw_hud()
        self.game.screen_draw()
        self.clock.tick(self.game.config.TICK)

    def draw_hud(self):
        for i in range(len(self.player_health)):
            if i >= self.player.hp:
                self.player_health[i].set_alpha(100)
            self.game.screen.blit(self.player_health[i], (0 + 30 * i, 0))
        if self.player_count == 2:
            for i in range(len(self.player2_health)):
                if i >= self.player2.hp:
                    self.player2_health[i].set_alpha(100)
                self.game.screen.blit(self.player2_health[i], (0 + 30 * i, 30))
        score_value = str(self.game.score if self.success else self.game.score + self.score)
        score = pg.font.Font(self.game.font, 20).render(score_value, 1, self.game.font_color)
        score_rect = score.get_rect()
        score_rect.topright = (630, 10)
        self.game.screen.blit(score, score_rect)

    def handle_enemy_touch(self):
        enemies = pg.sprite.spritecollide(self.player, self.game.enemies_list, False, pg.sprite.collide_mask)
        if enemies:
            self.player.hurt(1)
        if self.player_count == 2:
            enemies = pg.sprite.spritecollide(self.player2, self.game.enemies_list, False, pg.sprite.collide_mask)
            if enemies:
                self.player2.hurt(1)

    def handle_shooting(self):
        for enemy in self.game.enemies_list:
            bullets = pg.sprite.spritecollide(enemy, self.game.player_bullets_list, False, pg.sprite.collide_mask)
            for bullet in bullets:
                enemy.hp -= bullet.power
                self.game.hit_alt_sound.play()
                bullet.kill()
                if enemy.hp <= 0:
                    enemy.kill()
                    if isinstance(enemy, Boss):
                        self.game.boss_destroy_sound.play()
                        self.game.actual_level.score += 100 * self.player.hp
                        if self.player_count == 2:
                            self.game.actual_level.score += 100 * self.player2.hp
                        self.players_alive = 0
                        self.success = True
                    else:
                        self.game.actual_level.score += 10
        bullets = pg.sprite.spritecollide(self.player, self.game.enemy_bullets_list, False, pg.sprite.collide_mask)
        for bullet in bullets:
            self.player.hurt(bullet.power)
        if self.player_count == 2:
            bullets = pg.sprite.spritecollide(self.player2, self.game.enemy_bullets_list, False, pg.sprite.collide_mask)
            for bullet in bullets:
                self.player2.hurt(bullet.power)
