from colision_handler import colision_handler
from UI_handler import  UI_Handler
import pyxel
from blinky import blinky
from pacman import pacman
from HUD import HUD_obj
from fruit import fruit_object
class App():
    def __init__(self) -> None:
        #Select the pacman
        self.pacman = pacman
        pyxel.run(self.update,UI_Handler.draw)

    def update(self):
        if not pacman.game_end:
            #Check the input of the user
            self.pacman.change_direction()
            self.pacman.move()
            self.pacman.pellet_eaten_check()
            if pacman.fruit_spawned == True and fruit_object.cycle_counter <= 300:
                fruit_object.fruit_update()
                self.pacman.fruit_collision_check()
            else:
                fruit_object.cycle_counter = 0
                pacman.fruit_spawned = False
    
            #Update the high score if current score is higher than the highest score obatined before game over
            if pacman.score > HUD_obj.high_score:
                HUD_obj.high_score = pacman.score
        else:
            UI_Handler.victory_maze_update()

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

App()