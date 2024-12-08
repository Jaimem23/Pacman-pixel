from consumable import Consumable
class Pellets(Consumable):
    def __init__(self, x_pos, y_pos,eaten):
        super().__init__(x_pos, y_pos,eaten)