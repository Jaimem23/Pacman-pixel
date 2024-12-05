from colision_handler import colision_handler
from UI_handler import  UI_Handler
import pyxel
from blinky import blinky
from pacman import pacman
from HUD import HUD_obj
from fruit import fruit_object
from colision_handler import colision_handler
from maze_handler import maze
from ghost_handler import ghost_handler

class UpdateHandler:
    
    def update(self):
        
        ghost_handler.update_ghosts()

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
            #Condition to make the maze blink when pacman has eaten all pellets
            if maze.blink_control <= 120:
                maze.victory_maze_update()
            else:
                maze.blink_control = 0
                pacman.game_end = False
        #Missing the reset conditions (this causes the screen blinking)

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

Update_handler = UpdateHandler()