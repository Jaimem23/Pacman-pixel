from colision_handler import colision_handler
from UI_handler import UI_handler
import pyxel
from pacman import pacman
class App():
    def __init__(self) -> None:
        #Select the pacman
        self.pacman = pacman
        pyxel.run(self.update,UI_handler.draw)

    def update(self):
        #Check the input of the user
        self.pacman.change_direction()
        self.pacman.move()
        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()
    
App()