from consumable import Consumable

class PowerPellets(Consumable):
    def __init__(self, x_pos, y_pos, widht, height, eaten):
        super().__init__(x_pos, y_pos, widht, height, eaten)
    
    def activate_power():
        #Make the ghosts blink and change the pattern of them (still to be done)
        pass
