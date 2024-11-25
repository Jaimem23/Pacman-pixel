import pyxel
import constants
from pacman import pacman
from blinky import blinky

class UIHandler:
    def __init__(self):
        pyxel.init(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
        pyxel.load("assets/resources.pyxres")

    def draw(self):
        pyxel.cls(0)
        """x and y: The coordinates where the copied region will be drawn.
        img: The image or tilemap source (0-2 for image bank, 0-7 for tilemap).
        u and v: The coordinates of the top-left corner of the region to be copied within the image or tilemap.
        w and h: The width and height of the region to be copied.
        [colkey]: An optional color key (0-255) to use for transparency. If specified, pixels with this color value will be treated as transparent.
        [rotate]: An optional rotation angle (in degrees) to apply to the copied region.
        [scale]: An optional scale factor (1.0 = 100%) to apply to the copied region."""
        
        pyxel.blt(pacman.x_pos,pacman.y_pos,0,pacman.x_pos_tile,pacman.y_pos_tile,16,16,None,None,1.4)
        pyxel.blt(blinky.x_pos,blinky.y_pos,1,blinky.x_pos_tile,blinky.y_pos_tile,16,16,None,None,1.4)

UI_handler = UIHandler()