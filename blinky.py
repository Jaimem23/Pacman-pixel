from ghost import Ghost
from constants import BLINKY_Y_TILE
from pacman import pacman
import random
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)

    

    def change_direction(self):

        if self.__x_bias > self.__y_bias and self.__x_bias > 0:
            self.__next_direction = "right"

        if super().is_next_tile_wall(self._direction) and not super().remains_in_same_tile(self._direction):
            directions = ["right","left","up","down"]
            self._direction = directions[random.randint(0,3)]
        super().change_direction()
    
    
    #Read only properties
    @property
    def __x_bias(self):
        return int((pacman.x_pos - self.x_pos)/8)
    
    @property
    def __y_bias(self):
        return int((pacman.y_pos - self.y_pos)/8)

blinky = Blinky(80,160,16,16,0,BLINKY_Y_TILE,"right")