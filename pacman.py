from sprite import Sprite
from pyxel import btn,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT, \
                      KEY_W,KEY_S,KEY_A,KEY_D
from constants import SCREEN_HEIGHT,SCREEN_WIDTH, \
                        PACMAN_UP_TILE_Y, PACMAN_DOWN_TILE_Y, PACMAN_RIGHT_TILE_Y, PACMAN_LEFT_TILE_Y,PACMAN_INITIAL_X,PACMAN_INITIAL_Y
from maze_handler import maze
class Pacman(Sprite):
    def __init__(self, x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile,velocity: int):
        super().__init__(x_pos, y_pos, widht, height,x_pos_tile,y_pos_tile)
        self.direction = "right"
        self.velocity = velocity
        self.pellet_positions = maze.pellet_positions
        self.__eaten_pellets = []
        self.game_end = False
        #A variable to control the animations depending on the frames
        self.__animation_timer = 5
        self.__next_direction = self.direction
        
    def change_direction(self):
        """A function that cheks the direction of the pacman based on the input"""
        #Only change to that direction if he can move
        if self.__can_move(self.__next_direction):
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

    def move(self):
        """A function that moves pacman with his direction"""
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

        #Check if there's a pellet in the position and if there is, change the pellet status to eaten
        for element in self.pellet_positions:
            if (element.x_pos >= int(self.x_pos/8 + 1) and element.x_pos < int(self.x_pos/8 + 3)) and (element.y_pos >= int(self.y_pos/8 + 1) and element.y_pos < int(self.y_pos/8 + 3)):
                if not element.eaten:
                    element.eaten = True
                    self.__eaten_pellets.append(element)
        #If Pacman has eaten all of the pellets, the game ends
        if len(self.pellet_positions) == len(self.__eaten_pellets):

            #Select the required sprite for pacman on the victory screen according to the direction
            if self.direction.lower() == "up":
                self.x_pos_tile = 16
                self.y_pos_tile = 32
            elif self.direction.lower() == "down":
                self.x_pos_tile = 16
                self.y_pos_tile = 48
            elif self.direction.lower() == "right":
                self.x_pos_tile = 16
                self.y_pos_tile = 0
            elif self.direction.lower() == "left":
                self.x_pos_tile = 16
                self.y_pos_tile = 16

            #Change the direction by stand-by and set the game has ended
            self.direction = "stand-by"
            self.game_end = True
    
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
pacman = Pacman(PACMAN_INITIAL_X, PACMAN_INITIAL_Y, 8, 8, 0, 0, 2)