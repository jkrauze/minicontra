from weapon.bullet import Bullet


class SoldierBullet(Bullet):
    def __init__(self, game, center_x, center_y, way):
        super().__init__(game, 10, 1, center_x, center_y, way)
        print("bullet !1", center_x, center_y, way)

    def set_image(self):
        sprite = self.game.soldier_bullet_sprite
        if self.way[0] == 0:
            if self.way[1] == -1:
                self.image = sprite.subsurface((424, 13, 15, 15))
            else:
                self.image = sprite.subsurface((424, 60, 15, 15))
        elif self.way[0] == 1:
            if self.way[1] == 0:
                self.image = sprite.subsurface((448, 37, 15, 15))
            elif self.way[1] == -1:
                self.image = sprite.subsurface((448, 12, 15, 15))
            else:
                self.image = sprite.subsurface((448, 61, 15, 15))
        else:
            if self.way[1] == 0:
                self.image = sprite.subsurface((399, 37, 15, 15))
            elif self.way[1] == -1:
                self.image = sprite.subsurface((399, 12, 15, 15))
            else:
                self.image = sprite.subsurface((399, 61, 15, 15))
        return self.image