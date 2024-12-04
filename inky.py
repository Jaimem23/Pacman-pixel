from ghost import Ghost
import constants

class Inky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)

inky = Inky(constants.SCREEN_WIDTH/2 - 20,248,16,16,0,constants.BLINKY_Y_TILE,"up")