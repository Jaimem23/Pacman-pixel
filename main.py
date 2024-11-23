from colision_handler import ColisionHandler
from UI_handler import UIHandler
import pyxel
from pacman import Pacman

class App():
    def __init__(self) -> None:
        pyxel.init(120,160)
        pyxel.load("assets/pacman.pyxres")
        #Create the pacman
        self.pacman = Pacman(10,10,16,16,"pacman")

        pyxel.run(self.update,self.draw)

    def update(self):

        #Check the input of the user
        self.pacman.change_direction()
        self.pacman.move()
        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.pacman.x_pos,self.pacman.y_pos,0,0,0,16,16)

App()