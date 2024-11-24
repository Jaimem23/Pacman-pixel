from colision_handler import ColisionHandler
from UI_handler import UIHandler
import pyxel

class App:
    def __init__(self):
        pyxel.init(675, 900, "Pac-man")
        self.maze = UIHandler()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.maze.update()

    def draw(self):
        self.maze.draw()

App()