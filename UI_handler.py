import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAPTION, CHARACTERS, GAME_STARTING, GAME_RUNNING, GAME_LEVEL_UP, \
                        GAME_LIVE_LOST, GAME_OVER, PACMAN_DEATH_TILES_X, PACMAN_DEATH_TILES_Y
from pacman import pacman
from blinky import blinky
from maze_handler import maze
from HUD import HUD_obj
from fruit import fruit_object
from ghost_handler import ghost_handler
from update_handler import Update_handler
class UIHandler:
    ''' This class is in charge of drawing all of the visuals of the game '''

    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,CAPTION)
        pyxel.load("assets/resources.pyxres")
        maze.map_matrix_create()
        maze.create_ghost_map_matrix()
        self.pellet_position = maze.pellet_positions
        self.__characters = CHARACTERS
        self.__characters_drawn = 0
        self.fruit_counter = 0
 
    def maze_draw(self):
        '''This function is in charge of drawing the maze when the game is running'''
        pyxel.bltm(0, 50, 0, 0, 0, 448, 504, None, None, 1) #Temporarily edited, to do the collisions in a basic setting y is missing + 50


    def victory_maze_draw(self):
        '''This function is in charge of drawing the maze while the victory screen is running '''
        #This two elif control the timing of the map blink, when the variable blink_control divided by 20 returns a 
        #remainder bigger than or equal to 10 it will load the white map to create the effect
        
        if Update_handler.frame_counter%20 < 10:
            pyxel.bltm(0, 50, 0, 0, 512, 448, 504, None, None, 1)

        elif Update_handler.frame_counter%20 >= 10:
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
        #This structure is the same used to print all of the strings in the UI
        #The variable characters drawn is private and only serves to register 
        #the quantity of characters that have already been drawn
        self.__characters_drawn = 0
        for letter in ("HIGH SCORE"):
            #For every letter in the input string, the same code is used to draw the letter
            #However as seen in the x position, letters will be autonmatically indented
            #thanks and addition that depends on the quantity of characters drawn
            pyxel.blt(164+self.__characters_drawn*12,4,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,1)
            self.__characters_drawn += 1

        #Draw the high score numbers
        self.__characters_drawn = 0
        for number in str(HUD_obj.high_score):
            if self.__characters_drawn <= 8:
                #The structure used here is the same as explained previously, however the x position
                #is divided by 2 to ensure that as the string grows larger, the characters are still
                #centered under the word high score
                pyxel.blt(224-12*len(str(HUD_obj.high_score))/2+self.__characters_drawn*12,24,0,self.__characters[number][0],self.__characters[number][1],16,16,0,0,1)
                self.__characters_drawn += 1

        #Draw score letters
        self.__characters_drawn = 0
        for letter in ("SCORE"):
            pyxel.blt(43+self.__characters_drawn*12,4,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,1)
            self.__characters_drawn += 1

        #Score draw
        self.__characters_drawn = 0
        for number in str(HUD_obj.current_score):
            if self.__characters_drawn <= 8:
                pyxel.blt(73 - 12*len(str(HUD_obj.current_score))/2+self.__characters_drawn*12,24,0,self.__characters[number][0],self.__characters[number][1],16,16,0,0,1)
                self.__characters_drawn += 1

        #Draw lives letters
        self.__characters_drawn = 0
        for letter in ("LIVES"):
            pyxel.blt(345+self.__characters_drawn*12,4,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,1)
            self.__characters_drawn += 1  

        #Draw the lives icons
        for counter in range(pacman.lives):
            pyxel.blt(350+counter*20, 24, 0, 16, 0,16, 16, 0, 1)


    def ready_banner_draw (self):
        '''A function to draw the ready and level message at the start of a level'''

        #Draw LEVEL letters and number
        self.__characters_drawn = 0
        for letter in ("LEVEL " + str(HUD_obj.level)):
            pyxel.blt(160+self.__characters_drawn*20,223,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,2)
            self.__characters_drawn += 1

        #Draw READY letters
        self.__characters_drawn = 0
        for letter in ("READY"):
            pyxel.blt(176+self.__characters_drawn*20,263,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,2)
            self.__characters_drawn += 1

        #Draw the REGRESSIVE counter number
        pyxel.blt(216,291, 0,self.__characters[str(3 - (Update_handler.frame_counter// 30))][0],self.__characters[str(3 - (Update_handler.frame_counter// 30))][1],16,16,0,0,2)

    def pacman_death_draw (self):
        '''A function to draw the pacman death'''
        pyxel.blt(pacman.x_pos+ 7,pacman.y_pos + 55,0,PACMAN_DEATH_TILES_X[Update_handler.frame_counter//13],PACMAN_DEATH_TILES_Y,16,16, 0, 0, 1.4)

    def game_over_draw (self):
        #Draw GAME OVER letters
        self.__characters_drawn = 0
        for letter in ("GAME OVER"):
            pyxel.blt(132+self.__characters_drawn*20,263,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,2)
            self.__characters_drawn += 1

        #Draw PRESS S letters
        self.__characters_drawn = 0
        for letter in ("PRESS S"):
            pyxel.blt(148+self.__characters_drawn*20,290,0,self.__characters[letter][0],self.__characters[letter][1],16,16,0,0,2)
            self.__characters_drawn += 1
        

    def draw(self):
        pyxel.cls(0)
        if HUD_obj.game_state == GAME_STARTING:
            self.maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            self.ready_banner_draw()
            pyxel.blt(pacman.x_pos+ 7,pacman.y_pos + 55,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.4)


        elif HUD_obj.game_state == GAME_RUNNING:
            self.maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            if not fruit_object.eaten:
                self.fruit_draw()
            """x and y: The coordinates where the copied region will be drawn.
            img: The image or tilemap source (0-2 for image bank, 0-7 for tilemap).
            u and v: The coordinates of the top-left corner of the region to be copied within the image or tilemap.
            w and h: The width and height of the region to be copied.
            [colkey]: An optional color key (0-255) to use for transparency. If specified, pixels with this color value will be treated as transparent.
            [rotate]: An optional rotation angle (in degrees) to apply to the copied region.
            [scale]: An optional scale factor (1.0 = 100%) to apply to the copied region."""
            pyxel.blt(pacman.x_pos+ 7,pacman.y_pos + 55,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.4)
            ghost_handler.draw_ghosts()


        elif HUD_obj.game_state == GAME_LEVEL_UP:
            self.victory_maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            pyxel.blt(pacman.x_pos+ 7,pacman.y_pos + 55,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.4)


        elif HUD_obj.game_state == GAME_LIVE_LOST:
            self.maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            self.pacman_death_draw()


        elif HUD_obj.game_state == GAME_OVER:
            self.maze_draw()
            self.hud_draw()
            self.erase_eaten_pellets()
            self.game_over_draw()


UI_Handler = UIHandler()
