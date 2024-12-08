from ghost import Ghost
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, CLYDE_INITIAL_X, CLYDE_INITIAL_Y, CLYDE_Y_TILE
import pyxel
from pacman import pacman
class Clyde(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def reset(self):
        self.x_pos = CLYDE_INITIAL_X
        self.y_pos = CLYDE_INITIAL_Y
        super().reset()


    def change_target(self):
        if self.mode == "chase":
            #Calculate distance with pacman. Calculate the distance squared to simplify calculations
            dist_sqr = (pacman.x_pos - self.x_pos) ** 2 + (pacman.y_pos - self.y_pos) ** 2
            #Check if the distance is less than 8 tiles
            if dist_sqr > (8 * 8) ** 2: 
                self.target = [pacman.x_pos,pacman.y_pos]
            else: self.target = [0,SCREEN_HEIGHT]
        elif self.mode == "eaten":
            self.target = [int(SCREEN_WIDTH/2 - 16),int((SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [0,SCREEN_HEIGHT]
        elif self.mode == "exiting":
            self.target = [(SCREEN_WIDTH/2 - 16),(SCREEN_HEIGHT/2 - 106)]

clyde = Clyde(CLYDE_INITIAL_X,CLYDE_INITIAL_Y,16,16,0,CLYDE_Y_TILE,"right",450)