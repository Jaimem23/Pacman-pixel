from colision_handler import colision_handler
from UI_handler import  UI_Handler
import pyxel
from blinky import blinky
from pacman import pacman
from HUD import HUD_obj
from fruit import fruit_object
from colision_handler import colision_handler
class App():
    def __init__(self) -> None:
        pyxel.run(self.update,UI_Handler.draw)

    def update(self):
        #Check the input of the user
        pacman.change_direction()
        pacman.move()
        blinky.change_direction()
        blinky.change_mode()
        blinky.move()
        if not pacman.game_end:
            #Check the input of the user
            pacman.change_direction()
            pacman.move()
            colision_handler.pellet_eaten_check()
            if fruit_object.eaten == False and fruit_object.cycle_counter <= 300:
                fruit_object.fruit_update()
                colision_handler.fruit_collision_check()
            else:
                fruit_object.cycle_counter = 0
                fruit_object.eaten = True
    
            #Update the high score if current score is higher than the highest score obatined before game over
            if HUD_obj.level_score > HUD_obj.high_score:
                HUD_obj.high_score = HUD_obj.level_score
        else:
            UI_Handler.victory_maze_update()

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

App()