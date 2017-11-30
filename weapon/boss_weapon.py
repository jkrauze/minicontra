from weapon.boss_bullet import BossBullet
from weapon.enemy_weapon import EnemyWeapon


class BossWeapon(EnemyWeapon):
    def __init__(self, game):
        super().__init__(game, 90)

    def shoot(self, x, y, shoot_direction):
        self.game.enemy_bullets_list.add(BossBullet(self.game, x, y, (-5, -1)))
        self.game.enemy_bullets_list.add(BossBullet(self.game, x, y, (-5, 0)))
        self.game.enemy_bullets_list.add(BossBullet(self.game, x, y, (-5, 1)))
        self.game.shoot_alt_sound.play()
