import pyxel
from ghost import Ghost
from blinky import blinky
from constants import INKY_Y_TILE,SCREEN_WIDTH,SCREEN_HEIGHT, INKY_INITIAL_X, INKY_INITIAL_Y
from pacman import pacman


class Inky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def reset(self):
        '''A function that resets the parameters when restarting or leveling up'''
        self.x_pos = INKY_INITIAL_X
        self.y_pos = INKY_INITIAL_Y
        self.y_pos_tile = INKY_Y_TILE
        super().reset()

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
                self.target = [pacman.x_pos + inverted_vector[0], pacman.y_pos + inverted_vector[1]]

        elif self.mode == "eaten":
            self.target = [int(SCREEN_WIDTH/2 - 16),int((SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [SCREEN_WIDTH,SCREEN_HEIGHT]
        elif self.mode == "exiting":
            self.target = [int((SCREEN_WIDTH/2 - 16)),int((SCREEN_HEIGHT/2 - 106))]

inky = Inky(INKY_INITIAL_X,INKY_INITIAL_Y,16,16,0,INKY_Y_TILE,"up",300)