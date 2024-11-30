from sprite import Sprite
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from maze_handler import maze
from pacman import pacman
class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,direction):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile)
        self.direction = direction
        self.alive = True
        self.blinking = False
        self.velocity = 4
        self.__animation_speed = 2
        #A variable to control the animations depending on the frames
        self.__animation_timer = 5
        #Variables to change the direction of the ghost
        self.__pacman_x_pos = pacman.x_pos
        self.__pacman_y_pos = pacman.y_pos
        self.__next_direction = "right"


    #Read only properties
    @property
    def __x_bias(self):
        return int((self.__pacman_x_pos - self.x_pos)/8)
    
    @property
    def __y_bias(self):
        return int((self.__pacman_y_pos - self.y_pos)/8)

    @property
    def __map_matrix(self):
        return maze.map_matrix

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
    def blinking(self):
        return self.__blinking
    
    @alive.setter
    def blinking(self, blinking: bool):
        if not isinstance(blinking, bool):
            raise TypeError("The blinking attribute needs to have a boolean value, True or False")
        else: self.__blinking = blinking

    def move(self):
        """A function that moves the ghost"""
        if self.direction == "right":

            #Allow ghost to go from right to left
            if(self.x_pos > SCREEN_WIDTH):           
                self.x_pos = -self.width

            self.x_pos += 1 * self.velocity
            #Logic to make the animation of pacman moving the mouth
            #Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 16:self.x_pos_tile = 16
                else: self.x_pos_tile = 0

        elif self.direction == "left":
            #Allow pacman to go from left to right
            if(self.x_pos < -16):
                self.x_pos = SCREEN_WIDTH
            self.x_pos -= 1 * self.velocity

            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 48:self.x_pos_tile = 48
                else: self.x_pos_tile = 32

        elif self.direction == "up" and self.y_pos >= 0:

            #Need to substract one since the left corner is the origin
            self.y_pos -= 1 * self.velocity
                        #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 112:self.x_pos_tile = 112
                #Else, move to the previous one
                else: self.x_pos_tile = 96 
        elif self.direction == "down" and self.y_pos <= SCREEN_HEIGHT:
            self.y_pos += 1 * self.velocity
            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 80:self.x_pos_tile = 80
                else: self.x_pos_tile = 64
        # Increment animation timer, reset periodically
        self.__animation_timer = (self.__animation_timer + 1) % self.__animation_speed

    def change_direction(self):
        """A function that cheks the direction of the pacman based on the input"""
        #Only change to that direction if he can move
        if self.__can_move(self.__next_direction):
            self.direction = self.__next_direction
    
    def __can_move(self,direction):
        #Check the four tiles the pacman occupies
        for tile in range(4):
            if direction == "right" and self.__map_matrix[int(self.y_pos/8) + tile][int((self.x_pos/8) + 4)] != 0:
                #If a tile is a wall, return False
                return False
            elif direction == "left" and self.__map_matrix[int(self.y_pos/8) + tile][int((self.x_pos/8) - 1)] != 0:
                return False
            elif direction == "up" and self.__map_matrix[int(self.y_pos/8) -1][int((self.x_pos/8)) + tile] != 0:
                return False
            elif direction == "down" and self.__map_matrix[int(self.y_pos/8) +4][int((self.x_pos/8)) + tile] != 0:
                return False
        return True