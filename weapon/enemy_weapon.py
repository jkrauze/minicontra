import random
from weapon.weapon import Weapon


class EnemyWeapon(Weapon):
    def __init__(self, game, frequency):
        super().__init__(game, frequency)
        self.state = random.randint(0, frequency)

    def shoot(self, x, y, shoot_direction):
        raise NotImplementedError('shoot method must be implemented by weapon subclass')
