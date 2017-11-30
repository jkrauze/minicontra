from weapon.soldier_bullet import SoldierBullet
from weapon.enemy_weapon import EnemyWeapon


class SoldierWeapon(EnemyWeapon):
    def __init__(self, game):
        super().__init__(game, 60)

    def shoot(self, x, y, shoot_direction):
        self.game.enemy_bullets_list.add(SoldierBullet(self.game, x, y, shoot_direction))
        self.game.shoot_alt_sound.play()
