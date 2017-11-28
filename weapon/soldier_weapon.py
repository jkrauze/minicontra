from weapon.soldier_bullet import SoldierBullet
from weapon.weapon import Weapon


class SoldierWeapon(Weapon):
    def __init__(self, game):
        super().__init__(game, 60)

    def shoot(self, x, y, shoot_direction):
        self.game.enemy_bullets_list.add(SoldierBullet(self.game, x, y, shoot_direction))

    def handle_shooting(self, x, y, shoot_direction):
        super().handle_shooting(x,y,shoot_direction)
        super().start_shooting()
