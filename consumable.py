class Consumable:
    ''' A class that controls all of the consumables in the game, including pellets, power pellets and fruits'''
    
    def __init__(self, x_pos, y_pos, eaten):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.eaten = eaten

    @property
    def x_pos(self):
        return self.__x_pos
    
    @x_pos.setter
    def x_pos(self,x_pos):
        if not isinstance(x_pos,int):
            raise TypeError("x position must be an integer")
        
        self.__x_pos = x_pos

    @property
    def y_pos(self):
        return self.__y_pos
    
    @y_pos.setter
    def y_pos(self,y_pos):
        if not isinstance(y_pos,int):
            raise TypeError("y position must be an integer")
        
        self.__y_pos = y_pos

    @property
    def eaten(self):
        return self.__eaten
    
    @eaten.setter
    def eaten(self, eaten):
        if not isinstance(eaten, bool):
            raise TypeError("Eaten state must be a boolean")
        else:
            self.__eaten = eaten