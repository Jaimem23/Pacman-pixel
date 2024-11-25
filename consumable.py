from sprite import Sprite
class Consumable(Sprite):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile)
        self.eaten = False

    def despawn(self):
        self.x_pos_tile = 100
        self.y_pos_tile = 400
        self.eaten = True

    def spawn(self):
        self.eaten = False
