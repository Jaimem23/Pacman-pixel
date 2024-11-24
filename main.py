from colision_handler import ColisionHandler
from UI_handler import UIHandler
import pyxel
from pacman import Pacman
import constants
class App():
    def __init__(self) -> None:
        pyxel.init(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
        pyxel.load("assets/pacman.pyxres")
        #Create the pacman
        self.pacman = Pacman(10,10,16,16,"pacman",2)
        pyxel.run(self.update,self.draw)

    def update(self):
        #Check the input of the user
        self.pacman.change_direction()
        self.pacman.move()
        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.pacman.x_pos,self.pacman.y_pos,0,self.pacman.x_pos_tile,self.pacman.y_pos_tile,16,16)

App()