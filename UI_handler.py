import pyxel
import constants
from pacman import pacman
from blinky import blinky

class UIHandler:
    ''' This class is in charge of drawing all of the visuals of the game '''

    def __init__(self):
        self.blink_control = 0
        pyxel.init(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
        pyxel.load("assets/resources.pyxres")

    #This function is in charge of drawing the maze only when the game is started up or the maze needs to be reset
    def maze_draw(self):
        pyxel.cls(0)
        pyxel.bltm(68, 170, 0, 0, 0, 448, 504, None, None, 1.3)

    
    #This function is in charge of updating the parameters of the maze while the victory screen is running
    def victory_maze_update(self):
        pyxel.cls(0)
        if self.blink_control < 20:
            self.blink_control +=1

        #This else avoids the counter from surpassing 20 to save memory
        else:
            self.blink_control = 0

    #This function is in charge of drawing the maze while the victory screen is running
    def victory_maze_draw(self):
        #This two elif control the timing of the map blink, when the variable blink_control divided by 20 returns a 
        #remainder bigger than or equal to 10 it will load the white map to create the effect
        if self.blink_control%20 < 10:
            pyxel.bltm(114, 200, 0, 0, 512, 448, 504, None, None, 1.5)

        elif self.blink_control%20 >= 10:
            pyxel.bltm(114, 200, 0, 0, 0, 448, 504, None, None, 1.5)

    def draw(self):
        pyxel.cls(0)
        self.maze_draw()
        """x and y: The coordinates where the copied region will be drawn.
        img: The image or tilemap source (0-2 for image bank, 0-7 for tilemap).
        u and v: The coordinates of the top-left corner of the region to be copied within the image or tilemap.
        w and h: The width and height of the region to be copied.
        [colkey]: An optional color key (0-255) to use for transparency. If specified, pixels with this color value will be treated as transparent.
        [rotate]: An optional rotation angle (in degrees) to apply to the copied region.
        [scale]: An optional scale factor (1.0 = 100%) to apply to the copied region."""
        pyxel.blt(pacman.x_pos,pacman.y_pos,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16, 0, 0, 2.5)
        

UI_Handler = UIHandler()
