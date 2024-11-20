from colision_handler import ColisionHandler
from UI_handler import UIHandler
import pyxel
from pacman import Pacman

class main():
    def __init__(self) -> None:
        pyxel.init(120,160)
        #Create the pacman
        self.pacman = Pacman(0,0,16,16,"pacman")

        pyxel.run(self.update,self.draw)

    def update(self):

        #Check the input of the user

        if(pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)):
            self.pacman.direction = "up"
        elif(pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            self.pacman.direction = "left"
        elif(pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            self.pacman.direction = "right"
        elif(pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)):
            self.pacman.direction = "down"

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

main()