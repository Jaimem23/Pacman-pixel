from ghost import Ghost
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PINKY_INITIAL_X, PINKY_INITIAL_Y, PINKY_Y_TILE
from pacman import pacman

class Pinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

    def reset(self):
        '''A function that resets the parameters when restarting or leveling up'''
        self.x_pos = PINKY_INITIAL_X
        self.y_pos = PINKY_INITIAL_Y
        self.y_pos_tile = PINKY_Y_TILE
        super().reset()

    def change_target(self):
        if self.mode == "chase":
            #Get 3 tiles in from of pacman
            if(pacman.direction == "up"):
                self.target = [pacman.x_pos, pacman.y_pos - 3 * 8]
            elif(pacman.direction == "left"):
                self.target = [pacman.x_pos - 3 * 8, pacman.y_pos]
            elif (pacman.direction == "down"):
                self.target = [pacman.x_pos, pacman.y_pos + 3 * 8]
            else: self.target = [pacman.x_pos + 3 * 8, pacman.y_pos]
        elif self.mode == "eaten":
            self.target = [int(SCREEN_WIDTH/2 - 16),int((SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [0,0]
        elif self.mode == "exiting":
            self.target = [int((SCREEN_WIDTH/2 - 16)),int((SCREEN_HEIGHT/2 - 106))]

pinky = Pinky(PINKY_INITIAL_X,PINKY_INITIAL_Y,16,16,0,PINKY_Y_TILE,"right",150)

