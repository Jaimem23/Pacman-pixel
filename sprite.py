class Sprite:
    def __init__(self,x_pos:int,y_pos:int,widht:int,height:int,x_pos_tile:int,y_pos_tile:int):
        """A function to initialize the object attributes"""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = widht
        self.height = height
        self.x_pos_tile = x_pos_tile
        self.y_pos_tile = y_pos_tile

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
    def x_pos_tile(self):
        return self.__x_pos_tile
    
    @x_pos_tile.setter
    def x_pos_tile(self,tile):
        if not isinstance(tile,int):
            raise TypeError("x_pos_tile must be an integer")
        elif tile < 0:
            raise ValueError("x_pos_tile must be a non negative number")
        self.__x_pos_tile = tile

    @property
    def y_pos_tile(self):
        return self.__y_pos_tile
    
    @y_pos_tile.setter
    def y_pos_tile(self,tile):
        if not isinstance(tile,int):
            raise TypeError("y_pos_tile must be an integer")
        elif tile < 0:
            raise ValueError("y_pos_tile must be a non negative number")
        self.__y_pos_tile = tile