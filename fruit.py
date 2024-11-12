from consumable import Consumable

class Fruit(Consumable):
    def __init__(self, x_pos, y_pos, widht, height, image,value):
        super().__init__(x_pos, y_pos, widht, height, image)
        self.value = value