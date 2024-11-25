from consumable import Consumable

class PowerPellets(Consumable):
    def __init__(self, x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile):
        super().__init__(x_pos, y_pos, widht, height, x_pos_tile,y_pos_tile)
    
    def activate_power():
        #Make the ghosts blink and change the pattern of them
        pass
