from ghost import Ghost
from constants import BLINKY_Y_TILE
from pacman import pacman
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)

    def change_direction(self):
        self.__x_bias = pacman.x_pos - self.x_pos
        self.__y_bias = pacman.y_pos - self.y_pos

        if self.__x_bias > self.__y_bias and self.__x_bias > 0:
            self.__next_direction = "right"

        super().change_direction()

blinky = Blinky(100,100,16,16,0,BLINKY_Y_TILE,"right")