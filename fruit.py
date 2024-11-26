from consumable import Consumable
from constants import FRUIT_Y_TYLE
from HUD import HUD_obj
class Fruit(Consumable):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile):
        super().__init__(x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile)
        self.spawn()

    #Read only property
    @property
    def value(self):
       return self.__calculate_fruit_value()
    
    def spawn(self):
        #Import the function
        super().spawn()
        self.x_pos_tile = 0
        self.y_pos_tile = FRUIT_Y_TYLE

    def __calculate_fruit_value(self):
       return HUD_obj.level