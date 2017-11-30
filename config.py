import color as col
import pygame as pg
import configparser


class Config:
    SIZE = [640, 480]
    TICK = 60
    NAME = 'minicontra'

    def __init__(self, game):
        self.game = game
        self.file = 'settings.cfg'
        self.section = 'main'
        self.title = "options"
        self.WINDOW_SIZE = [640, 480]
        self.FULLSCREEN = False
        self.VIDEO_MODE = 0
        self.JUMP_PRECISION = 1.2
        self.BACKGROUND_COLOR = (5, 5, 50)
        self.KEY_UP = [pg.K_UP, pg.K_w]
        self.KEY_LEFT = [pg.K_LEFT, pg.K_a]
        self.KEY_DOWN = [pg.K_DOWN, pg.K_s]
        self.KEY_RIGHT = [pg.K_RIGHT, pg.K_d]
        self.KEY_JUMP = [pg.K_o, pg.K_1]
        self.KEY_SHOOT = [pg.K_p, pg.K_2]
        self.clock = pg.time.Clock()
        self.choose = 0
        self.option_keys = ['VIDEO_MODE', 'KEY_UP', 'KEY_LEFT', 'KEY_DOWN',
                            'KEY_RIGHT', 'KEY_JUMP', 'KEY_SHOOT']
        self.options = [s.replace('_', ' ') for s in self.option_keys]
        self.exit_option_index = len(self.option_keys)
        self.read()
        self.done = False
        self.changing = False
        self.choose_value = 0

    def get_option_value(self, key, i):
        if key.startswith("KEY_"):
            value = eval("self." + key)
            return "P{} {}".format(i + 1, pg.key.name(value[i]))
        elif i > 0:
            return
        elif key == 'VIDEO_MODE':
            if not self.changing or (self.changing and self.choose != 0):
                param = self.VIDEO_MODE
            else:
                param = self.choose_value
            if param == 0:
                return "Native resolution (640x480)"
            elif param == 1:
                return "Scale x2 (1280x960)"

    def run(self):
        self.done = False
        while not self.done:
            self.tick()

    def set_key(self):
        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        text = pg.font.Font(self.game.font, 40).render("Press key", 1, self.game.font_color_title)
        text_rect = text.get_rect()
        text_rect.center = (320, 240)
        self.game.screen.blit(text, text_rect)
        self.game.screen_draw()
        key_pressed = False
        while not key_pressed:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    exec('self.{}[{}] = {}'.format(self.option_keys[self.choose], self.choose_value, int(event.key)))
                    key_pressed = True
            self.clock.tick(self.TICK)

    def set_value(self):
        self.changing = True
        self.choose_value = 0
        if self.choose == 0:
            self.choose_value = self.VIDEO_MODE
        max_choose_value = 2
        while self.changing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.changing = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.changing = False
                    elif event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                        if self.choose == 0:
                            self.VIDEO_MODE = self.choose_value
                        else:
                            self.set_key()
                        self.write()
                        self.read()
                        self.changing = False
                    elif event.key == pg.K_LEFT:
                        self.choose_value = (self.choose_value - 1) % max_choose_value
                    elif event.key == pg.K_RIGHT:
                        self.choose_value = (self.choose_value + 1) % max_choose_value

            self.draw()
            self.game.screen_draw()
            self.clock.tick(self.game.config.TICK)

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.choose = self.exit_option_index
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.choose = self.exit_option_index
                    self.done = True
                elif event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                    if self.choose == self.exit_option_index:
                        self.done = True
                    else:
                        self.set_value()
                elif event.key == pg.K_UP:
                    self.choose = (self.choose - 1) % (len(self.options) + 1)
                elif event.key == pg.K_DOWN:
                    self.choose = (self.choose + 1) % (len(self.options) + 1)

        self.draw()
        self.game.screen_draw()
        self.clock.tick(self.game.config.TICK)

    def draw(self):
        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        self.game.screen.blit(
            pg.font.Font(self.game.font, 40).render(self.title, 1, self.game.font_color_title), (50, 50))
        for i in range(len(self.options)):
            self.game.screen.blit(
                pg.font.Font(self.game.font, 14).render(
                    self.options[i],
                    1,
                    self.game.font_color_not_active if self.changing else self.game.font_color if i != self.choose else self.game.font_color_choosed
                ), (50, 120 + 35 * i))
        for i in range(len(self.options)):
            self.game.screen.blit(
                pg.font.Font(self.game.font, 14).render(
                    self.get_option_value(self.option_keys[i], 0),
                    1,
                    (
                        self.game.font_color if self.choose > 0 and self.choose_value == 1 else self.game.font_color_choosed) if self.changing and self.choose == i else self.game.font_color_not_active
                ), (250, 120 + 35 * i))
        for i in range(len(self.options)):
            self.game.screen.blit(
                pg.font.Font(self.game.font, 14).render(
                    self.get_option_value(self.option_keys[i], 1),
                    1,
                    (
                        self.game.font_color if self.choose_value == 0 else self.game.font_color_choosed) if self.changing and self.choose == i else self.game.font_color_not_active
                ), (450, 120 + 35 * i))
        self.game.screen.blit(
            pg.font.Font(self.game.font, 20).render("Return to menu", 1,
                                                    self.game.font_color if self.exit_option_index != self.choose else self.game.font_color_choosed),
            (50, 420))

    def read(self):
        self.config = configparser.RawConfigParser()
        self.config.read(self.file)
        self.VIDEO_MODE = eval(self.config.get(self.section, 'video_mode'))
        self.WINDOW_SIZE = self.SIZE if self.VIDEO_MODE == 0 else [1280, 960]
        self.game.window = pg.display.set_mode(self.WINDOW_SIZE)
        self.KEY_UP = eval(self.config.get(self.section, 'key_up'))
        self.KEY_LEFT = eval(self.config.get(self.section, 'key_left'))
        self.KEY_DOWN = eval(self.config.get(self.section, 'key_down'))
        self.KEY_RIGHT = eval(self.config.get(self.section, 'key_right'))
        self.KEY_JUMP = eval(self.config.get(self.section, 'key_jump'))
        self.KEY_SHOOT = eval(self.config.get(self.section, 'key_shoot'))

    def write(self):
        for name in self.option_keys:
            self.config.set(self.section, name, eval('self.' + name))
        with open('settings.cfg', 'w') as file:
            self.config.write(file)
