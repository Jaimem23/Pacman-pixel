from ghost import Ghost
from constants import BLINKY_Y_TILE,SCREEN_WIDTH
from pacman import pacman
import random
import pyxel
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def change_mode(self):

        if pyxel.btn(pyxel.KEY_3):
            print("Change mode to eaten")
            self.mode = "eaten"
            self.__change_target()
        elif pyxel.btn(pyxel.KEY_4):
            print("Change mode to frightened")
            self.mode = "frightened"
            self.__change_target()

        if self.mode in ["scatter", "chase"] and self._timer_to_chg_mode != 0:
            self._timer_to_chg_mode = (self._timer_to_chg_mode + 1) % self._time_to_chg_mode
            return

        if self.mode == "scatter":
            print("Change mode to chase")
            self.mode = "chase"
            self._timer_to_chg_mode = 1
            self.__change_target()
        elif self.mode == "chase":
            print("Change mode to scatter")
            self.mode = "scatter"
            self._timer_to_chg_mode = 1
            self.__change_target()

    def __change_target(self):
        if self.mode == "chase":
            self.target = [pacman.x_pos,pacman.y_pos]
            self._change_direction_timer = 1
        elif self.mode == "eaten":
            self.target = [SCREEN_WIDTH/2,248]
            self._change_direction_timer = 1
        else:
            self.target = [SCREEN_WIDTH,0]
            self._change_direction_timer = 1

        
blinky = Blinky(88,160,16,16,0,BLINKY_Y_TILE,"right",0)
