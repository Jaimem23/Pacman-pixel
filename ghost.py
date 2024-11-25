from sprite import Sprite
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
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
            #Allow pacman to go from right to left
            if(self.x_pos > SCREEN_WIDTH):  
                #Make the ghost appear on the other side of the screen exactly the coordinates of its size
                #That way it gets teleported without the player noticing the change of coordinates            
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
        pass