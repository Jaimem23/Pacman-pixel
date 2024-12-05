from ghost import Ghost
import constants
import pyxel
from pacman import pacman
import constants

class Pinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def change_mode(self):

        if pyxel.btn(pyxel.KEY_3):
            print("Change mode to eaten")
            self.mode = "eaten"
        elif pyxel.btn(pyxel.KEY_4):
            print("Change mode to frightened")
            self.mode = "frightened"

        if self.mode in ["scatter", "chase"] and self._timer_to_chg_mode != 0:
            self._timer_to_chg_mode = (self._timer_to_chg_mode + 1) % self._time_to_chg_mode
            return

        if self.mode == "scatter":
            print("Change mode to chase")
            self.mode = "chase"
            self._timer_to_chg_mode = 1
        elif self.mode == "chase":
            print("Change mode to scatter")
            self.mode = "scatter"
            self._timer_to_chg_mode = 1

    def change_target(self):
        if self.mode == "chase":
            #Get 3 tiles in from of pacman
            if(pacman.direction == "up"):
                self.target = [pacman.x_pos, pacman.y_pos - 3 * 8]
            elif(pacman.direction == "left"):
                self.target = [pacman.x_pos - 3 * 8, pacman.y_pos]
            elif (pacman.direction == "down"):
                self.target = [pacman.x_pos, pacman.y_pos + 3 * 8]
            else: self.target = [pacman.x_pos + 3 * 8, pacman.y_pos]
        elif self.mode == "eaten":
            self.target = [constants.SCREEN_WIDTH/2,248]
        elif self.mode == "scatter":
            self.target = [0,0]

pinky = Pinky(int(constants.SCREEN_WIDTH/2 - 16),206,16,16,0,constants.PINKY_Y_TILE,"right",150)

