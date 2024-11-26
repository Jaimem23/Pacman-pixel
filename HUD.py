class HUD:
    def __init__(self):
        self.level = 1
    
    @property 
    def level(self):
        return self.__level

    @level.setter
    def level(self,level):
        if not isinstance(level,int):
            raise TypeError("Level must be an integer")
        elif level < 1:
            raise ValueError("Level must be a positive number")
        self.__level = level

    def increase_level(self):
        self.level += 1

HUD_obj = HUD()