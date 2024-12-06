from ghost import Ghost
import constants
import pyxel
from pacman import pacman
import constants
from blinky import blinky


class Inky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def change_target(self):
        if self.mode == "chase":

            #Calculate distance from blinky to pacman. Calculate the distance squared to simplify calculations
            dist_sqr = (pacman.x_pos - blinky.x_pos) ** 2 + (pacman.y_pos - blinky.y_pos) ** 2
            #If that distance is less than 8 tiles, go directly for pacman
            if dist_sqr < (8 * 8) ** 2: 
                self.target = [pacman.x_pos,pacman.y_pos]
            else:
                #Create a vector form pacman to blinky and rotate it 180 deg
                inverted_vector = (-(blinky.x_pos - pacman.x_pos),-(blinky.y_pos - pacman.x_pos))
                self.target[0] = [inverted_vector[0],inverted_vector[1]]

            self.target = [pacman.x_pos,pacman.y_pos]
        elif self.mode == "eaten":
            self.target = [int(constants.SCREEN_WIDTH/2 - 16),int((constants.SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT]
        elif self.mode == "exiting":
            self.target = [int((constants.SCREEN_WIDTH/2 - 16)),int((constants.SCREEN_HEIGHT/2 - 100))]

inky = Inky(int(constants.SCREEN_WIDTH/2) + 8,216,16,16,0,constants.INKY_Y_TILE,"up",300)