from weapon.bullet import Bullet


class SoldierBullet(Bullet):
    def __init__(self, game, center_x, center_y, way):
        super().__init__(game, 10, 1, center_x, center_y, way)

    def set_image(self):
        sprite = self.game.soldier_bullet_sprite
        if self.way[0] == 1:
            self.image = sprite.subsurface((448, 37, 15, 15))
        else:
            self.image = sprite.subsurface((399, 37, 15, 15))
        return self.image
