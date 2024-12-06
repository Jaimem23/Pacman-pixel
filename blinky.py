from ghost import Ghost
from constants import BLINKY_Y_TILE,SCREEN_WIDTH,SCREEN_HEIGHT
from pacman import pacman
import random
import pyxel
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def change_target(self):
        if self.mode == "chase":
            self.target = [pacman.x_pos,pacman.y_pos]
        elif self.mode == "eaten":
            self.target = [int(SCREEN_WIDTH/2 - 16),int((SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [SCREEN_WIDTH,0]
        elif self.mode == "exiting":
            self.target = [(SCREEN_WIDTH/2 - 16),(SCREEN_HEIGHT/2 - 100)]

        
blinky = Blinky(int(SCREEN_WIDTH/2 - 16),int(SCREEN_HEIGHT/2 - 100),16,16,0,BLINKY_Y_TILE,"right",1)
