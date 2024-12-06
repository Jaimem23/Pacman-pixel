from blinky import blinky
from pinky import pinky
from inky import inky
from clyde import clyde
import pyxel

class Ghost_Handler():
    def __init__(self) -> None:
        self.ghosts = (blinky,pinky,inky,clyde)
        self._timer_to_chg_mode = 1
        self._time_to_chg_mode = 300
        self._timer_frightened = 300
        self._time_frightened = 300
        self.__mode = "scatter"

    def update_ghosts(self):
        for ghost in self.ghosts:
            ghost.change_direction()
            ghost.change_target()
            ghost.move()
            ghost.check_colision()

    def activate_blink_mode(self):
        if pyxel.btn(pyxel.KEY_3):
            self._timer_frightened = 1
            for ghost in self.ghosts:
                ghost.blinking = True
                ghost.mode = "frightened"
            self.__mode = "frightened"


    def update_ghosts_mode(self):

        self._timer_frightened = self._timer_frightened  % self._time_frightened
        if self._timer_frightened != 0:
            self._timer_frightened += 1
            return
        elif self.__mode == "frightened" and self._timer_frightened == 0:
            for ghost in self.ghosts:
                ghost.blinking = False
                ghost.mode = "chase"
            self.__mode = "chase"
        

        #Wait for changing mode
        if self._timer_to_chg_mode != 0:
            self._timer_to_chg_mode = (self._timer_to_chg_mode + 1) % self._time_to_chg_mode
            return

        for ghost in self.ghosts:
            if self.__mode == "scatter" and ghost.mode not in ["frightened","exiting","eaten","waiting"]:
                print("Change to chase")
                ghost.change_mode("chase")
                self._timer_to_chg_mode = 1
            elif self.__mode == "chase" and ghost.mode not in ["frightened","exiting","eaten","waiting"]:
                print("Change to scatter")
                ghost.change_mode("scatter")
                self._timer_to_chg_mode = 1
        if self.__mode == "chase":
            self.__mode = "scatter"
        else: self.__mode = "chase"

            


        


    def draw_ghosts(self):
        for ghost in self.ghosts:
            pyxel.blt(ghost.x_pos + 7, ghost.y_pos + 55,1,ghost.x_pos_tile,ghost.y_pos_tile,16,16,0,0,1.4)

ghost_handler = Ghost_Handler()