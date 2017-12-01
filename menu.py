import pygame as pg
from config import Config


class Menu:
    def __init__(self, game, title, options, esc_option, additional_fields=None):
        self.game = game
        self.done = False
        self.additional_fields = additional_fields
        self.choose = 0
        self.title = title
        self.options = options
        self.esc_option = esc_option
        self.background_rect = self.game.menu_background.get_rect()
        self.background_animation = 0
        self.background_animation_way = -1
        self.is_main = title == Config.NAME
        if self.is_main:
            self.tick()
            self.game.screen_fadein()
            pg.event.clear()

    def run(self):
        self.done = False
        self.choose = 0
        pg.event.clear()
        while not self.done:
            self.tick()
        return self.choose

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.choose = self.esc_option
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                    self.done = True
                elif event.key == pg.K_ESCAPE:
                    if self.esc_option >= 0:
                        self.choose = self.esc_option
                        self.done = True
                elif event.key == pg.K_UP:
                    self.choose = (self.choose - 1) % len(self.options)
                elif event.key == pg.K_DOWN:
                    self.choose = (self.choose + 1) % len(self.options)

        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        if self.is_main:
            self.game.screen.blit(self.game.menu_background, self.background_rect)
            self.background_animation += 1
            if self.background_animation == 10:
                self.background_animation = 0
                self.background_rect.x += self.background_animation_way
                if self.background_rect.x == 0 or -self.background_rect.x == 1280 - Config.SIZE[0]:
                    self.background_animation_way = -self.background_animation_way
        self.draw()

        self.game.screen_draw()
        self.game.clock.tick(self.game.config.TICK)

    def draw(self):
        self.game.screen.blit(
            pg.font.Font(self.game.font, 40).render(self.title, 1, self.game.font_color_title), (50, 50))
        options_start = 200 + (0 if not self.additional_fields else len(self.additional_fields) * 40)
        if self.additional_fields:
            for i in range(len(self.additional_fields)):
                self.game.screen.blit(
                    pg.font.Font(self.game.font, 20).render(self.additional_fields[i][0], 1, self.game.font_color_not_active),
                    (50, 150 + 50 * i))
                self.game.screen.blit(
                    pg.font.Font(self.game.font, 20).render(self.additional_fields[i][1], 1, self.game.font_color_not_active),
                    (250, 150 + 50 * i))
        for i in range(len(self.options)):
            self.game.screen.blit(
                pg.font.Font(self.game.font, 20).render(self.options[i], 1,
                                                        self.game.font_color if i != self.choose else self.game.font_color_choosed),
                (50, options_start + 60 * i))
