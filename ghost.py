from sprite import Sprite
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from maze_handler import maze
from pacman import pacman
import random
import pyxel
class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction,time_to_start):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile)
        self.direction = direction
        self.__Y_POS_TILE = y_pos_tile
        self.alive = True
        self.frightened = False
        self.blinking = False
        self.__velocity = 2
        self.__animation_speed = 2
        #A variable to control the animations depending on the frames
        self.__animation_timer = 5
        #Variables to change the direction of the ghost
        self.__next_direction = "up"
        #Target the right top corner of the maze
        self.target = [0,SCREEN_WIDTH]
        self._change_direction_timer = 0
        self._change_direction_speed = int(8// (self.__velocity))
        #Variables to change mode
        self.mode = "waiting"  
        self._timer_to_start = 1
        self._time_to_start = time_to_start
        self.__going_up = False

    #Read only attributes
    @property
    def __map_matrix(self):
        if self.mode in ["exiting","eaten"]:
            return maze.ghost_map_matrix
        return maze.map_matrix

    @property 
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self,mode):
        if not isinstance(mode,str):
            raise TypeError("Ghost mode must be a str")
        elif mode.lower() not in ["scatter","chase","eaten","frightened","waiting","exiting"]:
            raise ValueError("Ghost mode must be scatter, chase, eaten, frightened or waiting,exitingg")
        
        self.__mode = mode.lower()

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self,direction):  
        if not isinstance(direction,str):
            raise TypeError("Direction must be an integer")
        #Change every direction to lower in order to avoid errors writting it in upperCase
        elif direction.lower() != "up" and direction.lower() != "down" and direction.lower() != "right" and direction.lower() != "left":
            raise ValueError("Direction must be 'up', 'down', 'left', or 'right'")
        else: self.__direction = direction.lower()
    
    @property
    def alive(self):
        return self.__alive
    
    @alive.setter
    def alive(self, alive: bool):
        if not isinstance(alive, bool):
            raise TypeError("The alive attribute needs to have a boolean value, True or False")
        else:
            self.__alive = alive
        
    @property
    def frightened(self):
        return self.__frightened
    
    @frightened.setter
    def frightened(self, frightened: bool):
        if not isinstance(frightened, bool):
            raise TypeError("The frightened attribute needs to have a boolean value, True or False")
        else: self.__frightened = frightened

    def get_eated(self):
        #self._change_direction_speed = 1
        self.alive = False
        self.mode = "eaten"
        self.__velocity = 6

    def move(self):
        """A function that moves the ghost"""

        if self.mode == "waiting":
            if self._timer_to_start != 0:
                
                if self.__going_up and self._timer_to_start % 4 == 0:
                    self.x_pos_tile = 96
                    self.__going_up = False
                elif not self.__going_up and self._timer_to_start % 4== 0:
                    self.x_pos_tile = 80
                    self.__going_up = True

                #Change position every 4 frames
                if self.__going_up:
                    self.y_pos = self.y_pos - self.__velocity
                else: self.y_pos = self.y_pos + self.__velocity

                #Update the time
                self._timer_to_start = (self._timer_to_start + 1) % self._time_to_start 

                #Dont check directions nor if there are walls 
                return     
            else: 
                self.mode = "exiting"
                self.target = [int((SCREEN_WIDTH/2 - 16)/8),int((SCREEN_HEIGHT/2 - 100)/8)]
        elif self.mode == "exiting":
            if int(self.x_pos/8) == int(self.target[0]/8) and  int(self.y_pos/8)  == int(self.target[1]/8):
                self.__velocity = 4
                self.mode = "chase"
        elif self.mode == "eaten":
            if int(self.x_pos/8) == int(self.target[0]/8) and  int(self.y_pos/8)  == int(self.target[1]/8):
                self.__velocity = 4
                self.alive = True
                self.frightened = False
                #Change mode to exiting
                self.mode = "exiting"
          
   
        if self.direction == "right" and self.__can_move(self.direction):

            #Allow ghost to go from right to left
            if(self.x_pos > SCREEN_WIDTH):           
                self.x_pos = -self.width

            self.x_pos += 1 * self.__velocity
            #Logic to make the animation of pacman moving the mouth
            #Only update every N frames
            if not self.alive:
                self.y_pos_tile = 80
                self.x_pos_tile = 0
            elif self.frightened and self.blinking and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 48:self.x_pos_tile += 16
                else: self.x_pos_tile = 0
            elif self.frightened and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 16:self.x_pos_tile = 16
                else: self.x_pos_tile = 0
            elif self.__animation_timer == 0:
                self.y_pos_tile = self.__Y_POS_TILE
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 16:self.x_pos_tile = 16
                else: self.x_pos_tile = 0
           
        elif self.direction == "left" and self.__can_move(self.direction):
            #Allow pacman to go from left to right
            if(self.x_pos < -16):
                self.x_pos = SCREEN_WIDTH
            self.x_pos -= 1 * self.__velocity

            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if not self.alive:
                self.y_pos_tile = 80
                self.x_pos_tile = 16
            elif self.frightened and self.blinking and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 48:self.x_pos_tile += 16
                else: self.x_pos_tile = 0
            elif self.frightened and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 16:self.x_pos_tile = 16
                else: self.x_pos_tile = 0
            elif self.__animation_timer == 0:
                self.y_pos_tile = self.__Y_POS_TILE
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 48:self.x_pos_tile = 48
                else: self.x_pos_tile = 32

        elif self.direction == "up" and self.__can_move(self.direction):

            #Need to substract one since the left corner is the origin
            self.y_pos -= 1 * self.__velocity
                        #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if not self.alive:
                self.y_pos_tile = 80
                self.x_pos_tile = 48
            elif self.frightened and self.blinking and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 48:self.x_pos_tile += 16
                else: self.x_pos_tile = 0
            elif self.frightened and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 16:self.x_pos_tile = 16
                else: self.x_pos_tile = 0
            elif self.__animation_timer == 0:
                self.y_pos_tile = self.__Y_POS_TILE
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 112:self.x_pos_tile = 112
                #Else, move to the previous one
                else: self.x_pos_tile = 96 

        elif self.direction == "down" and self.__can_move(self.direction):

            self.y_pos += 1 * self.__velocity
            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if not self.alive:
                self.y_pos_tile = 80
                self.x_pos_tile = 32
            elif self.frightened and self.blinking and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 48:self.x_pos_tile += 16
                else: self.x_pos_tile = 0
            elif self.frightened and self.__animation_timer == 0:
                self.y_pos_tile = 64
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 16:self.x_pos_tile = 16
                else: self.x_pos_tile = 0
            elif self.__animation_timer == 0:
                self.y_pos_tile = self.__Y_POS_TILE
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 80:self.x_pos_tile = 80
                else: self.x_pos_tile = 64

        # Increment animation timer, reset periodically
        self.__animation_timer = (self.__animation_timer + 1) % self.__animation_speed

    def change_mode(self,mode):
        "A function that changes the mode of the ghost given a mode"
        if mode == "scatter":
            self.mode = "scatter"
        elif mode == "chase":
            self.mode = "chase"

    def __calculate_new_direction(self):
        #If he has recently change its direction, return
        if self._change_direction_timer != 0 and self.mode != "eaten": 
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
            if self.__can_move_next_tile(direction): new_directions.append(direction)

        if len(new_directions) == 1: 
            #If you can only keep forward, skip this function
            if new_directions[0] == self.direction: return

        if self.mode == "frightened":
            self.__next_direction = new_directions[random.randrange(0,len(new_directions))]
            self._change_direction_timer = 1


        #If the mode is frightened it should not calculate the path
        if self.mode == "frightened": return

        #Calculate the best path
        self.__calculate_best_path(new_directions)
    
    def __can_move(self,direction):
        """A function that chekcs if the next step is a wall"""
        for tile in range(4): 
            if direction == "right" and self.__map_matrix[int(self.y_pos/8) + tile][int((self.x_pos+ 24 +self.__velocity)/8)] == 1:
                #If a tile is a wall, return False
                return False
            elif direction == "left" and self.__map_matrix[int((self.y_pos)/8) + tile][int((self.x_pos - self.__velocity)/8)] == 1:
                return False
            elif direction == "up" and self.__map_matrix[int((self.y_pos - self.__velocity)/8)][int((self.x_pos/8)) + tile] == 1:
                return False
            elif direction == "down" and self.__map_matrix[int((self.y_pos+  24 + self.__velocity)/8)][int((self.x_pos/8)) + tile] == 1:
                return False
        return True
    
    def __can_move_next_tile(self,direction):
        """A function that checks if the next tile is a wall"""
        for tile in range(4): 
            if direction == "right" and self.__map_matrix[int(self.y_pos/8) + tile][int((self.x_pos)/8) + 4] == 1:
                #If a tile is a wall, return False
                return False
            elif direction == "left" and self.__map_matrix[int(self.y_pos/8) + tile][int((self.x_pos)/8) - 1] == 1:
                return False
            elif direction == "up" and self.__map_matrix[int((self.y_pos/8) -1)][int((self.x_pos/8)) + tile] == 1:
                return False
            elif direction == "down" and self.__map_matrix[int((self.y_pos)/8) + 4][int((self.x_pos/8)) + tile] == 1:
                return False
        return True
    
    def __calculate_best_path(self,new_directions):
        """A function that changes the direction of the ghost given legal directions"""
        lowest_distance_sqr = float("inf")
        best_direction = "up"
        #For each direction in legal directions
        for direction in new_directions:
            if direction == "up":
                next_x = self.x_pos
                next_y = self.y_pos - self.__velocity
                #Calculate the distance squared to simplify calculations
                distance_sqr = (self.target[0] - next_x) ** 2 + (self.target[1] - next_y) ** 2
                if distance_sqr < lowest_distance_sqr:
                    lowest_distance_sqr = distance_sqr
                    best_direction = "up"
            elif direction == "left":
                next_x = self.x_pos - self.__velocity
                next_y = self.y_pos
                #Calculate the distance squared to simplify calculations
                distance_sqr = (self.target[0] - next_x) ** 2 + (self.target[1] - next_y) ** 2
                if distance_sqr < lowest_distance_sqr:
                    lowest_distance_sqr = distance_sqr
                    best_direction = "left"
            elif direction == "down": 
                next_x = self.x_pos
                next_y = self.y_pos + self.__velocity
                #Calculate the distance squared to simplify calculations
                distance_sqr = (self.target[0] - next_x) ** 2 + (self.target[1] - next_y) ** 2
                if distance_sqr < lowest_distance_sqr:
                    lowest_distance_sqr = distance_sqr
                    best_direction = "down"
            else: 
                next_x = self.x_pos + self.__velocity
                next_y = self.y_pos
                #Calculate the distance squared to simplify calculations
                distance_sqr = (self.target[0] - next_x) ** 2 + (self.target[1] - next_y) ** 2
                if distance_sqr < lowest_distance_sqr:
                    lowest_distance_sqr = distance_sqr
                    best_direction = "right"
            self.__next_direction = best_direction
            #Reset the timer to change direction
            self._change_direction_timer = 1

    def __remains_in_same_tile(self, direction):
        """A function that checks if the next step will stay in same tile"""
        current_tile = 0
        next_pos = 0
        new_tile = 0
        if direction == "right":
            current_tile = int(self.x_pos // 8)
            next_pos = self.x_pos + self.__velocity
            new_tile = int((next_pos) // 8)
        elif direction == "left":
            current_tile = int(self.x_pos // 8)
            next_pos = self.x_pos - self.__velocity
            new_tile = int((next_pos) // 8)
        elif direction == "up":
            current_tile = int(self.y_pos // 8)
            next_pos = self.y_pos - self.__velocity
            new_tile = int((next_pos) // 8)
        elif direction == "down":
            current_tile = int(self.y_pos // 8)
            next_pos = self.y_pos + self.__velocity
            new_tile = int((next_pos) // 8)

        return current_tile == new_tile

    def change_direction(self):
        """A function that changes the direction of the ghosts automatically"""
        #Only change to that direction if the next tile is not a wall and if it will change tile in the next step
        if  self.__can_move_next_tile(self.__next_direction) and not self.__remains_in_same_tile(self.direction):
            self.direction = self.__next_direction
        self.__calculate_new_direction()

    def check_colision(self):
        """A function that checks colision with pacman"""
        ghost_x_upper_bound,ghost_y_upper_bound = self.x_pos + 10,self.y_pos + 10
        ghost_x_lower_bound,ghost_y_lower_bound = self.x_pos + -10,self.y_pos -10

        #Return True if the have the same tile
        if pacman.x_pos > ghost_x_lower_bound and pacman.x_pos < ghost_x_upper_bound \
            and pacman.y_pos > ghost_y_lower_bound and pacman.y_pos < ghost_y_upper_bound\
            and self.mode not in ["frightened","eaten"]:
            pacman.die()
        elif pacman.x_pos > ghost_x_lower_bound and pacman.x_pos < ghost_x_upper_bound \
            and pacman.y_pos > ghost_y_lower_bound and pacman.y_pos < ghost_y_upper_bound\
            and self.mode == "frightened":
            self.get_eated()
    
    def change_velocity(self,velocity:int):
        self.__velocity = velocity

    def force_change_direction(self,new_direction:str):
        """A function that forces the ghost to change direction"""
        if self.mode in ["waiting","exiting","eaten"]:return

        self.direction = new_direction
        self.__next_direction = new_direction
        self._change_direction_timer = 1
    
        