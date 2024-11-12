from ghost import Ghost

class Clyde(Ghost):

    def __init__(self, x_pos, y_pos, widht, height, image):
        super().__init__(x_pos, y_pos, widht, height, image)
        self.alive = True
        self.blinking = False
    
    @property
    def alive(self):
        return self.__alive
    
    @alive.setter
    def alive(self, alive: bool):
        if not isinstance(alive, bool):
            raise TypeError("The alive attribute needs to have  a boolean value, True or False")
        
    @property
    def blinking(self):
        return self.__blinking
    
    @alive.setter
    def blinking(self, blinking: bool):
        if not isinstance(blinking, bool):
            raise TypeError("The blinking attribute needs to have  a boolean value, True or False")