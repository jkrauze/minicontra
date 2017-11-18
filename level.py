import pygame as pg
import configparser
from block import Block
from enemy import Enemy
from player import Player
from menu import Menu


class Level:
    def __init__(self, game, file):
        self.game = game
        self.file = file
        self.section = 'level'
        self.config = configparser.RawConfigParser()
        self.config.read(self.file)
        self.blocks = eval(self.config.get(self.section, 'blocks'))
        self.enemies = eval(self.config.get(self.section, 'enemies'))
        for block in self.blocks:
            Block(self.game, block[0], block[1], block[2], block[3])
        for enemy in self.enemies:
            Enemy(self.game, enemy[0], enemy[1], enemy[2])
        self.player = Player(self.game, 0)
        self.done = False
        self.return_state = 0
        self.clock = pg.time.Clock()

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
                print("quit")
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    while not self.done:
                        option = Menu(self.game, "Paused", ["Resume", "Restart", "Return to menu", "Exit game"]).run()
                        if option == 0:
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
        self.handle_shooting()

        pg.display.flip()
        self.clock.tick(self.game.config.TICK)

    def handle_shooting(self):
        for enemy in self.game.enemies_list:
            bullets = pg.sprite.spritecollide(enemy, self.game.player_bullets_list, False)
            for bullet in bullets:
                enemy.hp -= bullet.power
                bullet.kill()
                if enemy.hp <= 0:
                    enemy.kill()
