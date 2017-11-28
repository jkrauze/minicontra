class Weapon:
    def __init__(self, game, shooting_frequency):
        self.game = game
        self.shooting_frequency = shooting_frequency
        self.state = -1

    def start_shooting(self):
        if self.state == -1:
            self.state = 0

    def stop_shooting(self):
        if self.state > 0:
            self.state = -self.state
        elif self.state == 0:
            self.state = -1

    def shoot(self, x, y, shoot_direction):
        raise NotImplementedError('shoot method must be implemented by weapon subclass')

    def handle_shooting(self, x, y, shoot_direction):
        if self.state > 0:
            self.state -= 1
        elif self.state == 0:
            self.state = self.shooting_frequency
            self.shoot(x, y, shoot_direction)
        elif self.state < -1:
            self.state += 1
