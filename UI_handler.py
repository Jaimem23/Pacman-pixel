import pyxel
import constants
from pacman import pacman
from blinky import blinky
from maze_handler import maze
from HUD import HUD_obj
from fruit import fruit_object
class UIHandler:
    ''' This class is in charge of drawing all of the visuals of the game '''

    def __init__(self):
        pyxel.init(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT, constants.CAPTION)
        pyxel.load("assets/resources.pyxres")
        maze.map_matrix_create()
        self.pellet_position = maze.pellet_positions
        self.blink_control = 0
        self.__characters = {"H": (16, 96), "I": (32, 96), "G": (48,96), "L": (32, 144), "V": (48, 144), "M": (16, 160), "S": (0,80), "C": (16, 80), "O": (32, 80), "R": (48, 80),
                              "E": (0, 96), "A": (0, 160), "F":(32,160),"D": (64, 80), "Y": (64, 96), "0": (0, 112), "1": (16, 112), "2": (32,112), "3": (48, 112), "4": (0, 128), "5": (16, 128), "6": (32, 128), "7": (48, 128), 
                              "8": (0,144), "9": (16, 144), " ": (48, 160)}
        self.start_counter = 0
        self.__characters_drawn = 0
        self.fruit_counter = 0
 
        



    def maze_draw(self):
        '''This function is in charge of drawing the maze when the game is running'''
        pyxel.bltm(0, 50, 0, 0, 0, 448, 504, None, None, 1) #Temporarily edited, to do the collisions in a basic setting y is missing + 50

    def victory_maze_update(self):
        '''This function is in charge of updating the parameters of the maze while the victory screen is running'''
        if self.blink_control <= 120:
            self.blink_control +=1

        else:
            self.blink_control = 0
            pacman.game_end = False
            #Missing all of the reset conditions of level up IMPORTANT THIS CAUSES THE BLINK

    def victory_maze_draw(self):
        '''This function is in charge of drawing the maze while the victory screen is running '''
        #This two elif control the timing of the map blink, when the variable blink_control divided by 20 returns a 
        #remainder bigger than or equal to 10 it will load the white map to create the effect
        if self.blink_control%20 < 10:
            pyxel.bltm(0, 50, 0, 0, 512, 448, 504, None, None, 1)

        elif self.blink_control%20 >= 10:
            pyxel.bltm(0, 50, 0, 0, 0, 448, 504, None, None, 1)

    def fruit_draw(self):
        '''This function is in charge of drawing the fruit when a fruit has appeared'''
        pyxel.blt(fruit_object.x_pos + 7, fruit_object.y_pos + 55, 0, fruit_object.x_pos_tile, fruit_object.y_pos_tile, 16, 16, 0, 1.4)

    def erase_eaten_pellets (self):
        '''This function is in charge of darwing a black square in the positions where a pellet has been eaten'''
        for pellet in self.pellet_position:
            if pellet.eaten == True:
                #This instruction is used to paint a black square over the pellet position on those who have been eaten
                pyxel.rect(pellet.x_pos*8 - 4, pellet.y_pos*8 + 50, 10, 10, 0)
                
    def hud_draw(self):
        '''This function is in charge of drawing the score on screen'''

        #Draw high score letters
        self.__characters_drawn = 0
        for letter in ("HIGH SCORE"):
            pyxel.blt(164+self.__characters_drawn*12,4,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,1)
            self.__characters_drawn += 1

        #Draw the high score numbers
        self.__characters_drawn = 0
        for number in str(HUD_obj.high_score):
            if self.__characters_drawn <= 8:
                pyxel.blt(224-12*len(str(HUD_obj.high_score))/2+self.__characters_drawn*12,24,0,self.__characters[number][0],self.__characters[number][1],16,16,0,0,1)
                self.__characters_drawn += 1

        #Draw score letters
        self.__characters_drawn = 0
        for letter in ("SCORE"):
            pyxel.blt(43+self.__characters_drawn*12,4,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,1)
            self.__characters_drawn += 1


        #Score draw
        self.__characters_drawn = 0
        for number in str(pacman.score):
            if self.__characters_drawn <= 8:
                pyxel.blt(73 - 12*len(str(pacman.score))/2+self.__characters_drawn*12,24,0,self.__characters[number][0],self.__characters[number][1],16,16,0,0,1)
                self.__characters_drawn += 1

        #Draw lifes letters
        self.__characters_drawn = 0
        for letter in ("LIFES"):
            pyxel.blt(345+self.__characters_drawn*12,4,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,1)
            self.__characters_drawn += 1  

        #Draw the lifes icons
        for counter in range(pacman.lifes):
            pyxel.blt(350+counter*20, 24, 0, 16, 0,16, 16, 0, 1)


    def level_up_draw (self):
        #Draw ready
        self.__characters_drawn = 0
        for letter in ("READY"):
            pyxel.blt(176+self.__characters_drawn*20,263,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,2)
            self.__characters_drawn += 1
        #Draw the counter number
        pyxel.blt(216,291, 0,self.__characters[str(self.start_counter)][0],self.__characters[str(self.start_counter)][1],16,16,0,0,2)
        #Draw numbers of the counter 


    def draw(self):
        pyxel.cls(0)

        if not pacman.game_end:
            self.maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            if pacman.fruit_spawned:
                self.fruit_draw()
            """x and y: The coordinates where the copied region will be drawn.
            img: The image or tilemap source (0-2 for image bank, 0-7 for tilemap).
            u and v: The coordinates of the top-left corner of the region to be copied within the image or tilemap.
            w and h: The width and height of the region to be copied.
            [colkey]: An optional color key (0-255) to use for transparency. If specified, pixels with this color value will be treated as transparent.
            [rotate]: An optional rotation angle (in degrees) to apply to the copied region.
            [scale]: An optional scale factor (1.0 = 100%) to apply to the copied region."""
            pyxel.blt(pacman.x_pos+ 7,pacman.y_pos + 55,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.4)
            pyxel.blt(blinky.x_pos + 7, blinky.y_pos + 5,1,blinky.x_pos_tile,blinky.y_pos_tile,16,16,0,0,1.4)

        else:
            self.victory_maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            pyxel.blt(pacman.x_pos+ 7,pacman.y_pos + 55,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.4)
        

UI_Handler = UIHandler()
