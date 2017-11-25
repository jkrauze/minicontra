import pygame as pg
import color as col


class Menu:
    def __init__(self, game, title, options):
        self.game = game
        self.font = 'font/8-BIT WONDER.TTF'
        self.font_color = col.WHITE
        self.font_color_choosed = col.RED
        self.font_color_title = col.GREEN
        self.done = False
        self.clock = pg.time.Clock()
        self.choose = 0
        self.title = title
        self.options = options

    def run(self):
        while not self.done:
            self.tick()
        return self.choose

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                    self.done = True
                elif event.key == pg.K_UP:
                    self.choose = (self.choose - 1) % len(self.options)
                elif event.key == pg.K_DOWN:
                    self.choose = (self.choose + 1) % len(self.options)

        self.game.screen.fill(self.game.config.BACKGROUND_COLOR)
        self.draw()

        pg.display.flip()
        self.clock.tick(self.game.config.TICK)

    def draw(self):
        self.game.screen.blit(
            pg.font.Font(self.font, 40).render(self.title, 1, self.font_color_title), (50, 50))
        for i in range(len(self.options)):
            self.game.screen.blit(
                pg.font.Font(self.font, 20).render(self.options[i], 1,
                                                      self.font_color if i != self.choose else self.font_color_choosed),
                (50, 200 + 60 * i))
