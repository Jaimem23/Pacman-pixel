from constants import GAME_STARTING,GAME_LEVEL_UP,GAME_RUNNING, GAME_OVER
class HUD:
    def __init__(self):
        self.level = 1
        self.level_score = 0
        self.high_score = 0
        self.game_state = GAME_STARTING
    
    def increase_level(self):
        self.level += 1
        self.game_state = GAME_STARTING

    def score_update(self):
        if self.level_score > self.high_score:
            self.high_score = self.level_score


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

    @property
    def game_state(self):
        return self.__game_state
    
    @game_state.setter
    def game_state(self, game_state):
        if not isinstance(game_state, int):
            raise TypeError("The game state must be an integer number")
        elif game_state != GAME_STARTING and game_state != GAME_RUNNING and game_state != GAME_LEVEL_UP and game_state != GAME_OVER:
            raise ValueError("The game status maust be equal to one of the game screens")
        else:
            self.__game_state = game_state

HUD_obj = HUD()