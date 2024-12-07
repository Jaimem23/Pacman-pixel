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
        self.__chg_mode_counter = 0

    def update_ghosts(self):
        for ghost in self.ghosts:
            ghost.change_direction()
            ghost.change_target()
            ghost.move()
            ghost.check_colision()

    def activate_blink_mode(self):
        if pyxel.btn(pyxel.KEY_3):
            print("change to frightened")
            self._timer_frightened = 1
            for ghost in self.ghosts:
                if ghost.mode not in ["exiting","eaten","waiting"]:
                    ghost.blinking = True
                    ghost.mode = "frightened"
                    ghost.change_velocity(2)
                    ghost._change_direction_speed = 8
            self.__invert_direction()
            self.__mode = "frightened"


    def check_ghosts_moves(self):
        """Delete this function when the project is done"""
        if pyxel.btn(pyxel.KEY_5):
            for ghost in self.ghosts:
                print(ghost.mode)

    def __invert_direction(self):
       for ghost in self.ghosts:
            # Dictionary to map the current direction to its inverse
            direction_map = {
                "right": "left",
                "left": "right",
                "up": "down",
                "down": "up"
            }
            ghost.force_change_direction(direction_map[ghost.direction])

    def update_ghosts_mode(self):

        #Check if ghosts are frightened, so it does not change mode 
        self._timer_frightened = self._timer_frightened  % self._time_frightened
        if self._timer_frightened != 0:
            self._timer_frightened += 1
            return
        elif self.__mode == "frightened" and self._timer_frightened == 0:
            #Reset ghosts once the frightened mode is over
            for ghost in self.ghosts:
                ghost.blinking = False
                if ghost.mode not in ["eaten","waiting","exiting"]:
                    ghost.mode = "chase"
                    ghost.change_velocity(4)
            
            self.__invert_direction()
                    
            self.__mode = "chase"
        
        #Return if 4 loops have been completed
        if self.__chg_mode_counter > 4:return

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
        self.__invert_direction()
        if self.__mode == "chase":
            if self.__chg_mode_counter <= 4:
                self.__mode = "scatter"
                #Change when it should change mode again
                #Change 5 seconds to scatter
                self._time_to_chg_mode = 150
        else:
            if self.__chg_mode_counter <= 4:
                 
                self.__mode = "chase"
                #Change when it should change mode again. We should only count the loops
                self.__chg_mode_counter += 1

                #Change 20 seconds to chase
                self._time_to_chg_mode = 600



            


        


    def draw_ghosts(self):
        for ghost in self.ghosts:
            pyxel.blt(ghost.x_pos + 7, ghost.y_pos + 55,1,ghost.x_pos_tile,ghost.y_pos_tile,16,16,0,0,1.4)

ghost_handler = Ghost_Handler()