class HUD:
    def __init__(self):
        self.level = 1
        self.level_score = 0
        self.high_score = 0
    
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

    @property
    def high_score(self):
        return self.__high_score
    
    @high_score.setter
    def high_score(self, high_score):
        if not isinstance(high_score, int):
            raise TypeError("The score must be an integer")
        elif high_score < -1:
            raise ValueError("The high score must be a psoitive integer")
        else:
            self.__high_score = high_score

    def increase_level(self):
        self.level += 1


HUD_obj = HUD()