from weapon.bullet import Bullet


class BossBullet(Bullet):
    def __init__(self, game, center_x, center_y, way):
        super().__init__(game, 2, 1, center_x, center_y, way)

    def set_image(self):
        sprite = self.game.bullet_sprite
        if self.way[1] == 0:
            self.image = sprite.subsurface((399, 37, 15, 15))
        elif self.way[1] == -1:
            self.image = sprite.subsurface((399, 27, 15, 15))
        else:
            self.image = sprite.subsurface((399, 47, 15, 15))
        return self.image
