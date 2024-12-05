from blinky import blinky
from pinky import pinky
from inky import inky
from clyde import clyde
import pyxel

class Ghost_Handler():
    def __init__(self) -> None:
        self.ghosts = [blinky,pinky,inky,clyde]

    def update_ghosts(self):
        for ghost in self.ghosts:
            ghost.change_direction()
            ghost.change_mode()
            ghost.change_target()
            ghost.move()
            ghost.check_colision()

    def draw_ghosts(self):
        for ghost in self.ghosts:
            pyxel.blt(ghost.x_pos + 7, ghost.y_pos + 55,1,ghost.x_pos_tile,ghost.y_pos_tile,16,16,0,0,1.4)

ghost_handler = Ghost_Handler()