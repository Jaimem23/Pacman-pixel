"""Create classes to represent the objects needed for the final project. For all of them, create init
methods, properties and setters."""
from sprite import Sprite

class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, widht, height, image):
        super().__init__(x_pos, y_pos, widht, height, image)