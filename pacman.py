from sprite import Sprite
from pyxel import btn,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT, \
                      KEY_W,KEY_S,KEY_A,KEY_D,KEY_E
from constants import SCREEN_HEIGHT,SCREEN_WIDTH, \
                        PACMAN_UP_TILE_Y, PACMAN_DOWN_TILE_Y, PACMAN_RIGHT_TILE_Y, PACMAN_LEFT_TILE_Y,PACMAN_INITIAL_X,PACMAN_INITIAL_Y, FRUIT_X_POS, FRUIT_Y_POS
from maze_handler import maze
from fruit import fruit_object
class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,velocity: int):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile)
        self.direction = "right"
        self.velocity = velocity
        self.game_end = False
        self.lifes = 3

        #A variable to control the animations depending on the frames
        self.__animation_timer = 5
        self.__next_direction = self.direction
    
    def change_direction(self):
        """A function that cheks the direction of the pacman based on the input"""
        #Only change to that direction if the next tile is not a wall and if it will change tile in the next step
        if  self.__is_next_tile_wall(self.__next_direction) and not self.__is_centerd(self.direction):
            self.direction = self.__next_direction
            if self.direction == "right":
                self.y_pos_tile = PACMAN_RIGHT_TILE_Y
            elif self.direction == "left":
                self.y_pos_tile = PACMAN_LEFT_TILE_Y
            elif self.direction == "up":
                self.y_pos_tile = PACMAN_UP_TILE_Y
            elif self.direction == "down":
                #Change the direction of the sprite of the pacman
                self.y_pos_tile = PACMAN_DOWN_TILE_Y

        if(btn(KEY_W) or btn(KEY_UP)):
            #Change the direction the pacman wants to go
            self.__next_direction = "up"

        elif(btn(KEY_A) or btn(KEY_LEFT)):
            #Change the direction the pacman wants to go
            self.__next_direction = "left"


        elif(btn(KEY_D) or btn(KEY_RIGHT)):
            #Change the direction the pacman wants to go
            self.__next_direction = "right"


        elif(btn(KEY_S) or btn(KEY_DOWN)):
            #Change the direction the pacman wants to go
            self.__next_direction = "down"


    def __is_centerd(self, direction):
        current_tile = 0
        next_pos = 0
        new_tile = 0
        if direction == "right":
            current_tile = int(self.x_pos // 8)
            next_pos = self.x_pos + self.velocity + 4
            new_tile = int((next_pos) // 8)
        elif direction == "left":
            current_tile = int(self.x_pos // 8)
            next_pos = self.x_pos - self.velocity
            new_tile = int((next_pos) // 8)
        elif direction == "up":
            current_tile = int(self.y_pos // 8)
            next_pos = self.y_pos - self.velocity
            new_tile = int((next_pos) // 8)
        elif direction == "down":
            current_tile = int(self.y_pos // 8)
            next_pos = self.y_pos + self.velocity + 4
            new_tile = int((next_pos) // 8)
        
        if btn(KEY_E):
            print("Position is " + str(self.x_pos) + " and next position is " + str(next_pos))
            print("Current tile is " +  str(current_tile) + " and new tile is " + str(new_tile))
            print(self.__next_direction)
            print(self.direction)

        return current_tile == new_tile


    def move(self):
        """A function that moves pacman with his direction"""
        if(btn(KEY_E)):
            print(self.x_pos)
            print(self.y_pos)

        if self.direction == "right"  and self.__can_move(self.direction):
            #Allow pacman to go from right to left
            if(self.x_pos > SCREEN_WIDTH):  
                #Make the pacman appear on the other side of the screen exactly the coordinates of its size
                #That way it gets teleported without the player noticing the change of coordinates            
                self.x_pos = -self.width
            self.x_pos += 1 * self.velocity
            #Logic to make the animation of pacman moving the mouth
            #Only update every N frames

            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 32:
                    self.x_pos_tile += 16
                else: 
                    self.x_pos_tile = 0
        elif self.direction == "left" and self.__can_move(self.direction):
            #Allow pacman to go from left to right
            if(self.x_pos < -16):
                self.x_pos = SCREEN_WIDTH
            self.x_pos -= 1 * self.velocity

            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 32:
                    self.x_pos_tile += 16
                else: 
                    self.x_pos_tile = 0
        elif self.direction == "up" and self.__can_move(self.direction):
            #Need to substract one since the left corner is the origin
            self.y_pos -= 1 * self.velocity 
            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 32:
                    self.x_pos_tile += 16
                else: 
                    self.x_pos_tile = 0
        elif self.direction == "down" and self.__can_move(self.direction):
            self.y_pos += 1 * self.velocity

            #Logic to make the animation of pacman moving the mouth
            # Only update every N frames
            if self.__animation_timer == 0:
                #If is not the last sprite, move to the next one  
                if self.x_pos_tile != 32:
                    self.x_pos_tile += 16
                else: 
                    self.x_pos_tile = 0
        
        # Increment animation timer, reset periodically
        self.__animation_timer = (self.__animation_timer + 1) % self.__animation_speed


    
    @property
    def velocity(self):
        return self.__velocity
    
    @velocity.setter
    def velocity(self,velocity):
        if not isinstance(velocity, int):
            TypeError("Velocity must be an integer")
        elif velocity <= 1:
            ValueError("Velocity must be 1 or more")
        else:
            self.__velocity = velocity

    def __is_next_tile_wall(self,direction):
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

    def __can_move(self,direction):
        """A function that chekcs if the next step is a wall"""

        for tile in range(4): 
            if direction == "right" and self.__map_matrix[int(self.y_pos/8) + tile][int((self.x_pos+ 24 +self.velocity + 4)/8)] == 1:
                #If a tile is a wall, return False
                return False
            elif direction == "left" and self.__map_matrix[int((self.y_pos)/8) + tile][int((self.x_pos - self.velocity)/8)] == 1:
                return False
            elif direction == "up" and self.__map_matrix[int((self.y_pos - self.velocity)/8)][int((self.x_pos/8)) + tile] == 1:
                return False
            elif direction == "down" and self.__map_matrix[int((self.y_pos+  24 + self.velocity)/8)][int((self.x_pos/8)) + tile] == 1:
                return False
        return True
        
    #read only properties
    @property
    def __animation_speed(self):
        return 2

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self,direction):  
        if not isinstance(direction,str):
            raise TypeError("Direction must be an string")
        #Change every direction to lower in order to avoid errors if you write it in upperCase
        elif direction.lower() != "up" and direction.lower() != "down" and direction.lower() != "right" and direction.lower() != "left" and direction.lower() != "stand-by":
            raise ValueError("Direction must be 'up', 'down', 'left', or 'right'")
        else: self.__direction = direction.lower()

    #Read only properties
    @property
    def x_pos_tile(self):
        return self.__x_pos_tile
    
    @x_pos_tile.setter
    def x_pos_tile(self,tile):
        self.__x_pos_tile = tile

    @property
    def y_pos_tile(self):
        return self.__y_pos_tile
    
    @y_pos_tile.setter
    def y_pos_tile(self,tile):
        self.__y_pos_tile = tile
    
    #Read only properties
    @property
    def __map_matrix(self):
        return maze.map_matrix


#Create the pacman
pacman = Pacman(PACMAN_INITIAL_X, PACMAN_INITIAL_Y, 8, 8, 0, 0, 4)