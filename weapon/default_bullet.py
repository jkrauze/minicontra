from weapon.bullet import Bullet


class DefaultBullet(Bullet):
    def __init__(self, game, center_x, center_y, way):
        super().__init__(game, 10, 1, center_x, center_y, way)

    def set_image(self):
        if self.way[0] == 0:
            if self.way[1] == -1:
                self.image = self.game.bullet_sprite.subsurface((424, 13, 15, 15))
            else:
                self.image = self.game.bullet_sprite.subsurface((424, 60, 15, 15))
        elif self.way[0] == 1:
            if self.way[1] == 0:
                self.image = self.game.bullet_sprite.subsurface((448, 37, 15, 15))
            elif self.way[1] == -1:
                self.image = self.game.bullet_sprite.subsurface((448, 12, 15, 15))
            else:
                self.image = self.game.bullet_sprite.subsurface((448, 61, 15, 15))
        else:
            if self.way[1] == 0:
                self.image = self.game.bullet_sprite.subsurface((399, 37, 15, 15))
            elif self.way[1] == -1:
                self.image = self.game.bullet_sprite.subsurface((399, 12, 15, 15))
            else:
                self.image = self.game.bullet_sprite.subsurface((399, 61, 15, 15))
        return self.image