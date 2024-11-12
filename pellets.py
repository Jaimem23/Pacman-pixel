from consumable import Consumable
class Pellets(Consumable):
    def __init__(self, x_pos, y_pos, widht, height, image):
        super().__init__(x_pos, y_pos, widht, height, image)