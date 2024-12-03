from ghost import Ghost
from constants import BLINKY_Y_TILE,SCREEN_HEIGHT,SCREEN_WIDTH
from pacman import pacman
import random
import pyxel
class Blinky(Ghost):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction)
        self.mode = "frightened"
        #Target the right top corner of the maze
        self.target = [0,SCREEN_WIDTH]
        self._change_direction_timer = 0
        self._change_direction_speed = int(8 // self.velocity)
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

    def calculate_new_direction(self):
        #If he has recently change its direction, return
        if self._change_direction_timer != 0: 
            self._change_direction_timer = (self._change_direction_timer + 1) % self._change_direction_speed
            return

        if pyxel.btn(pyxel.KEY_E):
            print("Next tile is wall: " + str(super().can_move_next_tile(self.direction)) + " and it remains in same tile " + str(self.remains_in_same_tile(self.direction)) + \
                  " and can move: " + str(super().can_move(self.direction)))
            print("My position is " + str((self.x_pos,self.y_pos)) + " and my direction is " +str(self.direction))
        """if self.__x_bias > self.__y_bias and self.__x_bias > 0:
            self.next_direction = "right"""

       
        if self.mode == "frightened":
            directions = ["right","left","up","down"]
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
                if super().can_move_next_tile(direction): new_directions.append(direction)
            
            if len(new_directions) == 1: 
                #If you can only keep forward, skip this function
                if new_directions[0] == self.direction: return
            self.next_direction = new_directions[random.randrange(0,len(new_directions))]
            self._change_direction_timer = 1
    

    def change_direction(self):
        #Change direction only if he can move there and it is centered
        super().change_direction()
        self.calculate_new_direction()
    
    #Read only properties
    @property
    def __x_bias(self):
        return int((pacman.x_pos - self.x_pos)/8)
    
    @property
    def __y_bias(self):
        return int((pacman.y_pos - self.y_pos)/8)

blinky = Blinky(88,160,16,16,0,BLINKY_Y_TILE,"right")