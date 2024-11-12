class Sprite:
    def __init__(self,x_pos:int,y_pos:int,widht:int,height:int,image):
        """A function to initialize the object attributes"""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.widht = widht
        self.height = height
        self.image = image

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
    def widht(self):
        return self.__widht
    
    @widht.setter
    def widht(self,widht):
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