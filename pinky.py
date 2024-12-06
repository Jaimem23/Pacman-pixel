from ghost import Ghost
import constants
import pyxel
from pacman import pacman
import constants

class Pinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,_time_to_start)

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
            self.target = [int(constants.SCREEN_WIDTH/2 - 16),int((constants.SCREEN_HEIGHT/2) -60)]
        elif self.mode == "scatter":
            self.target = [0,0]
        elif self.mode == "exiting":
            self.target = [int((constants.SCREEN_WIDTH/2 - 16)),int((constants.SCREEN_HEIGHT/2 - 100))]

pinky = Pinky(int(constants.SCREEN_WIDTH/2 - 16),206,16,16,0,constants.PINKY_Y_TILE,"right",150)

