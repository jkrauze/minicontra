import configparser
from block import Block
from enemy import Enemy


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

    def update(self):
        pass

    def draw(self, screen):
        pass
