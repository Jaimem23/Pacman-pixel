from ghost import Ghost
import constants
import pyxel
from pacman import pacman
class Clyde(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)


    def change_target(self):
        if self.mode == "chase":
            #Calculate distance with pacman. Calculate the distance squared to simplify calculations
            dist_sqr = (pacman.x_pos - self.x_pos) ** 2 + (pacman.y_pos - self.y_pos) ** 2
            #Check if the distance is less than 8 tiles
            if dist_sqr > (8 * 8) ** 2: 
                self.target = [pacman.x_pos,pacman.y_pos]
            else: self.target = [0,constants.SCREEN_HEIGHT]
        elif self.mode == "eaten":
            self.target = [int(constants.SCREEN_WIDTH/2 - 16),int((constants.SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [0,constants.SCREEN_HEIGHT]
        elif self.mode == "exiting":
            self.target = [(constants.SCREEN_WIDTH/2 - 16),(constants.SCREEN_HEIGHT/2 - 106)]

clyde = Clyde(int(constants.SCREEN_WIDTH/2 - 42),216,16,16,0,constants.CLYDE_Y_TILE,"right",450)