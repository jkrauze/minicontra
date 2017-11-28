from weapon.default_bullet import DefaultBullet
from weapon.weapon import Weapon


class DefaultWeapon(Weapon):
    def __init__(self, game):
        super().__init__(game, 10)

    def shoot(self, x, y, shoot_direction):
        self.game.player_bullets_list.add(DefaultBullet(self.game, x, y, shoot_direction))
