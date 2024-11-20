from sprite import Sprite

class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, widht, height, image,direction):
        super().__init__(x_pos, y_pos, widht, height, image)
        self.direction = direction
        self.alive = True
        self.blinking = False
    
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self,direction):  
        if not isinstance(direction,str):
            raise TypeError("Direction must be an integer")
        #Change every direction to lower in order to avoid errors writting it in upperCase
        elif direction.lower() != "up" and direction.lower() != "down" and direction.lower() != "right" and direction.lower() != "left":
            raise ValueError("Direction must be 'up', 'down', 'left', or 'right'")
        else: self.__direction = direction.lower()
    
    @property
    def alive(self):
        return self.__alive
    
    @alive.setter
    def alive(self, alive: bool):
        if not isinstance(alive, bool):
            raise TypeError("The alive attribute needs to have a boolean value, True or False")
        else:
            self.__alive = alive
        
    @property
    def blinking(self):
        return self.__blinking
    
    @alive.setter
    def blinking(self, blinking: bool):
        if not isinstance(blinking, bool):
            raise TypeError("The blinking attribute needs to have a boolean value, True or False")
        else: self.__blinking = blinking