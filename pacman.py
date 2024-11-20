"""Create classes to represent the objects needed for the final project. For all of them, create init
methods, properties and setters."""
from sprite import Sprite

class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, widht, height, image,direction):
        super().__init__(x_pos, y_pos, widht, height, image)
        self.direction = direction
    
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self,direction):  
        if not isinstance(direction,str):
            raise TypeError("Direction must be an string")
        #Change every direction to lower in order to avoid errors if you write it in upperCase
        elif direction.lower() != "up" and direction.lower() != "down" and direction.lower() != "right" and direction.lower() != "left":
            raise ValueError("Direction must be 'up', 'down', 'left', or 'right'")
        else: self.__direction = direction.lower()