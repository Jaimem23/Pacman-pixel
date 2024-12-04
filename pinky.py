from ghost import Ghost
import constants
class Pinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)

pinky = Pinky(88,160,16,16,0,constants.PINKY_Y_TILE,"right")

