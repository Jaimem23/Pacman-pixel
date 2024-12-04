from ghost import Ghost
from constants import BLINKY_Y_TILE,SCREEN_WIDTH
from pacman import pacman
import random
import pyxel
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)
        self.mode = "frightened"
        #Target the right top corner of the maze
        self.target = [0,SCREEN_WIDTH]
        
    @property 
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self,mode):
        if not isinstance(mode,str):
            raise TypeError("Ghost mode must be a str")
        elif mode.lower() != "scatter" and mode.lower() != "chase" and mode.lower() != "eaten" and mode.lower() != "frightened":
            raise ValueError("Ghost mode must be scatter, chase, eaten or frightened")
        
        self.__mode = mode.lower()

    def change_mode(self):
        if pyxel.btn(pyxel.KEY_1):
            print("Change mode to chase")
            self.mode = "chase"
        elif pyxel.btn(pyxel.KEY_2):
            print("Change mode to frightened")
            self.mode = "frightened"
        elif pyxel.btn(pyxel.KEY_3):
            print("Change mode to eaten")
            self.mode = "eaten"
        elif pyxel.btn(pyxel.KEY_4):
            print("Change mode to scatter")
            self.mode = "scatter"
        
    def calculate_new_direction(self):
        #If he has recently change its direction, return
        if self._change_direction_timer != 0: 
            self._change_direction_timer = (self._change_direction_timer + 1) % self._change_direction_speed
            return

        directions = ["right","left","up","down"]

        #Check which directions are valid

        #remove the direction it is currently going, since it cannot move backwards
        if self.direction == "right":
            directions.remove("left")
        elif self.direction == "left":
            directions.remove("right")
        elif self.direction == "up":
            directions.remove("down")
        else: directions.remove("up")

        new_directions =[]
        #Check if which directions are allowed
        for direction in directions:
            if self.can_move_next_tile(direction): new_directions.append(direction)

        if len(new_directions) == 1: 
            #If you can only keep forward, skip this function
            if new_directions[0] == self.direction: return


        if self.mode == "frightened":
            self.next_direction = new_directions[random.randrange(0,len(new_directions))]
            self._change_direction_timer = 1
        elif self.mode == "chase":
            self.target = [pacman.x_pos,pacman.y_pos]
            self._change_direction_timer = 1
        elif self.mode == "eaten":
            self.target = [SCREEN_WIDTH/2,248]
            self._change_direction_timer = 1
        else:
            self.target = [SCREEN_WIDTH,0]
            self._change_direction_timer = 1

        #If the mode is frightened it should not calculate the path
        if self.mode == "frightened": return

        #Calculate the best path
        self.calculate_best_path(new_directions)

    def change_direction(self):
        #Only change to that direction if the next tile is not a wall and if it will change tile in the next step
        if  self.can_move_next_tile(self.next_direction) and not self.remains_in_same_tile(self.direction):
            self.direction = self.next_direction
        self.calculate_new_direction()
    


blinky = Blinky(88,160,16,16,0,BLINKY_Y_TILE,"right")