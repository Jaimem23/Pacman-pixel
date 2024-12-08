from ghost import Ghost
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BLINKY_INITIAL_X, BLINKY_INITIAL_Y, BLINKY_Y_TILE
from pacman import pacman
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def reset(self):
        self.x_pos = BLINKY_INITIAL_X
        self.y_pos = BLINKY_INITIAL_Y
        self.y_pos_tile = BLINKY_Y_TILE
        super().reset()

    def change_target(self):
        if self.mode == "chase":
            self.target = [pacman.x_pos,pacman.y_pos]
        elif self.mode == "eaten":
            self.target = [int(SCREEN_WIDTH/2 - 16),int((SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [SCREEN_WIDTH,0]
        elif self.mode == "exiting":
            self.target = [(SCREEN_WIDTH/2 - 16),(SCREEN_HEIGHT/2 - 106)]

        
blinky = Blinky(BLINKY_INITIAL_X,BLINKY_INITIAL_Y,16,16,0,BLINKY_Y_TILE,"right",1)


 