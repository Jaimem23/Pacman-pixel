import pyxel
import constants
from pacman import pacman
from blinky import blinky
from maze_handler import maze

class UIHandler:
    ''' This class is in charge of drawing all of the visuals of the game '''

    def __init__(self):
        pyxel.init(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
        pyxel.load("assets/resources.pyxres")
        maze.map_matrix_create()
        maze.pellet_list_create()
        self.pellet_position = maze.pellet_positions
        self.blink_control = 0
 
        



    def maze_draw(self):
        '''This function is in charge of drawing the maze when the game is running'''
        pyxel.bltm(0, 50, 0, 0, 0, 448, 504, None, None, 1) #Temporarily edited, to do the collisions in a basic setting y is missing + 50

    def victory_maze_update(self):
        '''This function is in charge of updating the parameters of the maze while the victory screen is running'''
        pyxel.cls(0)
        if self.blink_control < 20:
            self.blink_control +=1

        #This else avoids the counter from surpassing 20 to save memory
        else:
            self.blink_control = 0

    def victory_maze_draw(self):
        '''This function is in charge of drawing the maze while the victory screen is running '''
        #This two elif control the timing of the map blink, when the variable blink_control divided by 20 returns a 
        #remainder bigger than or equal to 10 it will load the white map to create the effect
        if self.blink_control%20 < 10:
            pyxel.bltm(0, 50, 0, 0, 512, 448, 504, None, None, 1)

        elif self.blink_control%20 >= 10:
            pyxel.bltm(0, 50, 0, 0, 0, 448, 504, None, None, 1)

    def erase_eaten_pellets (self):
        '''This function is in charge of darwing a black square in the positions where a pellet has been eaten'''
        for pellet in self.pellet_position:
            if pellet.eaten == True:
                #This instruction is used to paint a black square over the pellet position on those who have been eaten
                pyxel.rect(pellet.x_pos*8 - 4, pellet.y_pos*8 + 52, 8, 8, 0)
                
        
    def draw(self):
        if not pacman.game_end:
            pyxel.cls(0)
            self.maze_draw()
            self.erase_eaten_pellets()
            """x and y: The coordinates where the copied region will be drawn.
            img: The image or tilemap source (0-2 for image bank, 0-7 for tilemap).
            u and v: The coordinates of the top-left corner of the region to be copied within the image or tilemap.
            w and h: The width and height of the region to be copied.
            [colkey]: An optional color key (0-255) to use for transparency. If specified, pixels with this color value will be treated as transparent.
            [rotate]: An optional rotation angle (in degrees) to apply to the copied region.
            [scale]: An optional scale factor (1.0 = 100%) to apply to the copied region."""
            pyxel.blt(pacman.x_pos+ 2,pacman.y_pos + 54,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.5)
        else:
            self.victory_maze_draw()
            self.erase_eaten_pellets()
            pyxel.blt(pacman.x_pos+ 2,pacman.y_pos + 54,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 1.5)
        

UI_Handler = UIHandler()
