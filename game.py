import pygame as pg
import os
import config as c
import color as col
from level import Level
from menu import Menu


class Game:
    def __init__(self):
        pg.mixer.pre_init(frequency=44100, size=16, channels=2, buffer=1024)
        pg.init()
        self.font = os.path.join('font', '8-BIT WONDER.TTF')
        self.font_color = col.WHITE
        self.font_color_not_active = col.GRAY
        self.font_color_choosed = col.RED
        self.font_color_title = col.BLUE
        self.highscore_file_path = ".game.score"
        if not os.path.isfile(self.highscore_file_path):
            with open(self.highscore_file_path, 'w') as file:
                file.write('0')
        with open(self.highscore_file_path, 'r') as file:
            self.highscore = int(file.read())
        self.score = 0
        self.config = c.Config(self)
        self.screen = pg.Surface(self.config.SIZE)
        self.window_size = self.config.WINDOW_SIZE
        self.window = pg.display.set_mode(self.config.WINDOW_SIZE)
        pg.display.set_caption(self.config.NAME)

        self.win_sound = pg.mixer.Sound(os.path.join('snd', 'Jingle_Achievement_01.ogg'))
        self.win_sound.set_volume(0.9)
        self.lose_sound = pg.mixer.Sound(os.path.join('snd', 'Jingle_Lose_00.ogg'))
        self.lose_sound.set_volume(0.9)

        self.shoot_sound = pg.mixer.Sound(os.path.join('snd', 'Open_00.ogg'))
        self.shoot_sound.set_volume(0.8)
        self.shoot_alt_sound = pg.mixer.Sound(os.path.join('snd', 'Open_01.ogg'))
        self.shoot_alt_sound.set_volume(0.6)

        self.hit_sound = pg.mixer.Sound(os.path.join('snd', 'Hit_02.ogg'))
        self.hit_sound.set_volume(0.8)
        self.hit_alt_sound = pg.mixer.Sound(os.path.join('snd', 'Hit_01.ogg'))
        self.hit_alt_sound.set_volume(0.6)

        self.boss_destroy_sound = pg.mixer.Sound(os.path.join('snd', 'Explosion_00.ogg'))
        self.boss_destroy_sound.set_volume(0.8)

        self.ground_sprite = pg.image.load(os.path.join('img', 'ground3T.png'))
        self.ground_sprite.set_colorkey(self.ground_sprite.get_at((17, 1)))
        self.ground_sprite = pg.transform.scale2x(self.ground_sprite)

        self.player_sprite = pg.image.load(os.path.join('img', 'OpenGunnerHeroVer2.png')).convert()
        self.player_sprite.set_colorkey(self.player_sprite.get_at((1, 1)))
        self.player_subsprites = [self.player_sprite.subsurface((137, 683, 50, 50)),
                                  self.player_sprite.subsurface((137, 746, 50, 50)),
                                  self.player_sprite.subsurface((193, 683, 50, 50)),
                                  self.player_sprite.subsurface((193, 746, 50, 50)),
                                  self.player_sprite.subsurface((126, 143, 50, 50)),
                                  self.player_sprite.subsurface((331, 925, 50, 50)),
                                  self.player_sprite.subsurface((760, 925, 50, 50)),
                                  self.player_sprite.subsurface((126, 200, 50, 50)),
                                  self.player_sprite.subsurface((331, 1063, 50, 50)),
                                  self.player_sprite.subsurface((760, 1063, 50, 50)),
                                  self.player_sprite.subsurface((24, 143, 50, 50)),
                                  self.player_sprite.subsurface((137, 683, 50, 50)),
                                  self.player_sprite.subsurface((137, 746, 50, 50)),
                                  self.player_sprite.subsurface((24, 200, 50, 50)),
                                  self.player_sprite.subsurface((193, 683, 50, 50)),
                                  self.player_sprite.subsurface((193, 746, 50, 50)),
                                  [self.player_sprite.subsurface((24 + 51 * i, 315, 50, 50)) for i in range(8)],
                                  [self.player_sprite.subsurface((25 + 51 * i, 932, 50, 50)) for i in range(8)],
                                  [self.player_sprite.subsurface((454 + 51 * i, 932, 50, 50)) for i in range(8)],
                                  [self.player_sprite.subsurface((24 + 51 * i, 375, 50, 50)) for i in range(8)],
                                  [self.player_sprite.subsurface((25 + 51 * i, 1070, 50, 50)) for i in range(8)],
                                  [self.player_sprite.subsurface((454 + 51 * i, 1070, 50, 50)) for i in range(8)]]

        self.player2_sprite = pg.image.load(os.path.join('img', 'OpenGunnerHeroVer2_2.png')).convert()
        self.player2_sprite.set_colorkey(self.player2_sprite.get_at((1, 1)))
        self.player2_subsprites = [self.player2_sprite.subsurface((137, 683, 50, 50)),
                                  self.player2_sprite.subsurface((137, 746, 50, 50)),
                                  self.player2_sprite.subsurface((193, 683, 50, 50)),
                                  self.player2_sprite.subsurface((193, 746, 50, 50)),
                                  self.player2_sprite.subsurface((126, 143, 50, 50)),
                                  self.player2_sprite.subsurface((331, 925, 50, 50)),
                                  self.player2_sprite.subsurface((760, 925, 50, 50)),
                                  self.player2_sprite.subsurface((126, 200, 50, 50)),
                                  self.player2_sprite.subsurface((331, 1063, 50, 50)),
                                  self.player2_sprite.subsurface((760, 1063, 50, 50)),
                                  self.player2_sprite.subsurface((24, 143, 50, 50)),
                                  self.player2_sprite.subsurface((137, 683, 50, 50)),
                                  self.player2_sprite.subsurface((137, 746, 50, 50)),
                                  self.player2_sprite.subsurface((24, 200, 50, 50)),
                                  self.player2_sprite.subsurface((193, 683, 50, 50)),
                                  self.player2_sprite.subsurface((193, 746, 50, 50)),
                                  [self.player2_sprite.subsurface((24 + 51 * i, 315, 50, 50)) for i in range(8)],
                                  [self.player2_sprite.subsurface((25 + 51 * i, 932, 50, 50)) for i in range(8)],
                                  [self.player2_sprite.subsurface((454 + 51 * i, 932, 50, 50)) for i in range(8)],
                                  [self.player2_sprite.subsurface((24 + 51 * i, 375, 50, 50)) for i in range(8)],
                                  [self.player2_sprite.subsurface((25 + 51 * i, 1070, 50, 50)) for i in range(8)],
                                  [self.player2_sprite.subsurface((454 + 51 * i, 1070, 50, 50)) for i in range(8)]]

        self.enemy_sprite = pg.image.load(os.path.join('img', 'OpenGunnerEnemySoldier.png')).convert()
        self.enemy_sprite.set_colorkey(self.enemy_sprite.get_at((1, 1)))
        self.enemy_subsprites = [[self.enemy_sprite.subsurface((24 + 51 * i, 286, 50, 50)) for i in range(8)],
                                 [self.enemy_sprite.subsurface((24 + 51 * i, 346, 50, 50)) for i in range(8)],
                                 self.enemy_sprite.subsurface((24, 186, 50, 50))]

        self.boss_sprite = pg.image.load(os.path.join('img', 'OpenGunnerMechs.png')).convert()
        self.boss_sprite.set_colorkey(self.boss_sprite.get_at((1, 1)))
        self.boss_subsprites = [self.boss_sprite.subsurface((136, 155, 140, 108)),
                                self.boss_sprite.subsurface((136, 267, 140, 108)),
                                self.boss_sprite.subsurface((277, 267, 140, 108))]

        self.bullet_sprite = pg.image.load(os.path.join('img', 'M484BulletCollection2.png')).convert()
        self.bullet_sprite.set_colorkey(self.bullet_sprite.get_at((1, 1)))
        self.soldier_bullet_sprite = pg.image.load(os.path.join('img', 'M484BulletCollection2_modified1.png')).convert()
        self.soldier_bullet_sprite.set_colorkey(self.soldier_bullet_sprite.get_at((1, 1)))

        self.background = pg.image.load(os.path.join('img', '11-Mid-Night.png'))
        self.background.set_alpha(64)

        self.menu_background = pg.image.load(os.path.join('img', '01-Early-Morning.png'))
        self.menu_background.set_alpha(128)

        self.background_list = pg.sprite.Group()
        self.block_list = pg.sprite.Group()
        self.player_bullets_list = pg.sprite.Group()
        self.enemy_bullets_list = pg.sprite.Group()
        self.enemies_list = pg.sprite.Group()
        self.players_list = pg.sprite.Group()
        self.sprites_list = pg.sprite.Group()
        self.actual_level = None

        self.done = False

    def screen_draw(self):
        if self.config.VIDEO_MODE == 0:
            self.window.blit(self.screen, (0, 0))
        else:
            pg.transform.scale2x(self.screen, self.window)
        pg.display.flip()

    def screen_fadein(self):
        clock = pg.time.Clock()
        screen_copy = self.screen.copy()
        surface = pg.Surface(self.config.SIZE)
        surface.fill(col.BLACK)
        for i in range(255, -1, -5):
            surface.set_alpha(i)
            self.screen.blit(screen_copy, (0, 0))
            self.screen.blit(surface, (0, 0))
            self.screen_draw()
            clock.tick(60)

    def screen_fadeout(self):
        clock = pg.time.Clock()
        surface = pg.Surface(self.config.SIZE)
        surface.fill(col.BLACK)
        for i in range(0, 255, 5):
            surface.set_alpha(i)
            self.screen.blit(surface, (0, 0))
            self.screen_draw()
            clock.tick(60)

    def run(self):
        main_menu = Menu(self, self.config.NAME, ["Single player", "Two players", "Options", "Exit"], -1)
        pg.mixer.music.load(os.path.join('snd', 'menu.ogg'))
        pg.mixer.music.set_volume(0.7)
        pg.mixer.music.play(-1)
        while not self.done:
            option = main_menu.run()
            if option == 0 or option == 1:
                players_count = option + 1
                self.screen_fadeout()
                while not self.done:
                    self.score = 0
                    pg.mixer.music.stop()
                    for file in sorted(os.listdir('lvl')):
                        if file.endswith(".lvl"):
                            self.actual_level = Level(self, "lvl/" + file, players_count)
                            option = self.actual_level.run()
                            if not self.actual_level.success:
                                break

                    if self.actual_level.success:
                        if self.score > self.highscore:
                            with open(self.highscore_file_path, 'w') as file:
                                file.write(str(self.score))
                        pg.mixer.music.load(os.path.join('snd', 'end.ogg'))
                        pg.mixer.music.set_volume(0.7)
                        pg.mixer.music.play(-1)
                        score_results = [["score", str(self.score)], ["highscore", str(self.highscore)]]
                        option = Menu(self, "The End", ["Start again", "Return to menu", "Exit game"], -1,
                                      additional_fields=score_results).run()
                    elif option == 0:
                        self.lose_sound.play()
                        option = Menu(self, "Game Over", ["Try again", "Return to menu", "Exit game"], -1).run()
                    else:
                        option -= 1
                    if option == 1:
                        pg.mixer.music.load(os.path.join('snd', 'menu.ogg'))
                        pg.mixer.music.set_volume(0.7)
                        pg.mixer.music.play(-1)
                        break
                    elif option == 2:
                        self.done = True
            elif option == 2:
                self.config.run()
            else:
                break
        self.screen_fadeout()
        pg.quit()
