"""Create classes to represent the objects needed for the final project. For all of them, create init
methods, properties and setters."""
from sprite import Sprite
from pyxel import btn,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT, \
                      KEY_W,KEY_S,KEY_A,KEY_D
class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, widht, height, image,direction:str = "right"):
        super().__init__(x_pos, y_pos, widht, height, image)
        self.direction = direction
    
    def change_direction(self):
        """A function that cheks the direction of the pacman based on the input"""
        if(btn(KEY_W) or btn(KEY_UP)):
            self.direction = "up"
        elif(btn(KEY_A) or btn(KEY_LEFT)):
            self.direction = "left"
        elif(btn(KEY_D) or btn(KEY_RIGHT)):
            self.direction = "right"
        elif(btn(KEY_S) or btn(KEY_DOWN)):
            self.direction = "down"

    def move(self):
        "A function that moves pacman with his direction"
        if self.direction == "right":
            self.x_pos += 1
        elif self.direction == "left":
            self.x_pos -= 1
        elif self.direction == "up":
            #Need to substract one since the left corner is the origin
            self.y_pos -= 1
        else:
            self.y_pos += 1

        


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