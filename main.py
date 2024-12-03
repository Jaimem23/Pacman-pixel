from colision_handler import colision_handler
from UI_handler import  UI_Handler
import pyxel
from blinky import blinky
from pacman import pacman
class App():
    def __init__(self) -> None:
        #Select the pacman
        self.pacman = pacman
        pyxel.run(self.update,UI_Handler.draw)

    def update(self):
        if not pacman.game_end:
            #Check the input of the user
            self.pacman.change_direction()
            self.pacman.move()
            blinky.change_direction()
            blinky.move()
        else:
            UI_Handler.victory_maze_update()

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

App()