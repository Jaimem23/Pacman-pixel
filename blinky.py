from ghost import Ghost
from constants import BLINKY_Y_TILE,SCREEN_WIDTH
from pacman import pacman
import random
import pyxel
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def change_mode(self):
        if pyxel.btn(pyxel.KEY_1):
            print("Change mode to chase")
            self.mode = "chase"
        elif pyxel.btn(pyxel.KEY_2):
            print("Change mode to frightened")
            self.mode = "frightened"
        elif pyxel.btn(pyxel.KEY_3):
            print("Change mode to eaten")
            self.mode = "eaten"
        elif pyxel.btn(pyxel.KEY_4):
            print("Change mode to scatter")
            self.mode = "scatter"
        
    
    


blinky = Blinky(88,160,16,16,0,BLINKY_Y_TILE,"right",0)