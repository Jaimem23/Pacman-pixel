class Consumable:
    def __init__(self, x_pos, y_pos, width, height, eaten):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
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
    def width(self):
        return self.__widht
    
    @width.setter
    def width(self,widht):
        if not isinstance(widht,int):
            raise TypeError("widht value must be an integer")
        elif widht < 0:
            raise ValueError("Widht must be positive or 0 ")
        self.__widht = widht

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,height):
        if not isinstance(height,int):
            raise TypeError("Height value must be an integer")
        elif height < 0:
            raise ValueError("Height must be positive or 0 ")
        self.__height = height

    @property
    def eaten(self):
        return self.__eaten
    
    @eaten.setter
    def eaten(self, eaten):
        if not isinstance(eaten, bool):
            raise TypeError("Eaten state must be a boolean")
        else:
            self.__eaten = eaten