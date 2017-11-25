import pygame as pg
import color as col
import configparser
from block import Block
from platform import Platform
from enemy import Enemy
from player import Player
from menu import Menu


class Level:
    def __init__(self, game, file_path):
        self.game = game
        self.file_path = file_path
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 0):
                for pos, char in enumerate(line, 0):
                    if char == 'b':
                        Block(self.game, 32, 32, 32 * pos, 32 * line_num)
                    elif char == 'p':
                        Platform(self.game, 32, 32, 32 * pos, 32 * line_num)
                    elif char == 'e':
                        Enemy(self.game, 1, 32 * pos, 32 * line_num)
                    elif char == 'x':
                        self.player = Player(self.game, 0, 32 * pos, 32 * line_num)
        self.done = False
        self.return_state = 0
        self.clock = pg.time.Clock()
        self.player_health = [pg.image.load('img/heart.png').convert(),
                              pg.image.load('img/heart.png').convert(),
                              pg.image.load('img/heart.png').convert()]
        for elem in self.player_health:
            elem.set_colorkey(col.BLACK)

    def run(self):
        while not self.done:
            self.tick()
        self.game.block_list.empty()
        self.game.player_bullets_list.empty()
        self.game.enemies_list.empty()
        self.game.sprites_list.empty()
        return self.return_state

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    while not self.done:
                        option = Menu(self.game, "Paused", ["Resume", "Restart", "Return to menu", "Exit game"]).run()
                        if option == 0:
                            self.player.stop()
                            break
                        self.done = True
                        self.return_state = option
                        return
                else:
                    self.player.handle_keydown(event.key)
            elif event.type == pg.KEYUP:
                self.player.handle_keyup(event.key)

        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        self.game.sprites_list.update()
        self.game.sprites_list.draw(self.game.screen)
        self.game.enemies_list.draw(self.game.screen)
        self.game.players_list.draw(self.game.screen)
        self.handle_enemy_touch()
        self.handle_shooting()
        self.draw_hud()

        pg.display.flip()
        self.clock.tick(self.game.config.TICK)

    def draw_hud(self):
        for i in range(len(self.player_health)):
            if i >= self.player.hp:
                self.player_health[i].set_alpha(100)
            self.game.screen.blit(self.player_health[i], (10 + 30 * i, 10))

    def handle_enemy_touch(self):
        enemies = pg.sprite.spritecollide(self.player, self.game.enemies_list, False)
        if enemies:
            self.player.hurt(1)

    def handle_shooting(self):
        for enemy in self.game.enemies_list:
            bullets = pg.sprite.spritecollide(enemy, self.game.player_bullets_list, False)
            for bullet in bullets:
                enemy.hp -= bullet.power
                bullet.kill()
                if enemy.hp <= 0:
                    enemy.kill()
