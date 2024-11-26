from ghost import Ghost
from constants import BLINKY_Y_TILE
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)

blinky = Blinky(100,100,16,16,0,BLINKY_Y_TILE,"right")