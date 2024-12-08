from colision_handler import colision_handler
import pyxel
from blinky import blinky
from pacman import pacman
from HUD import HUD_obj
from fruit import fruit_object
from colision_handler import colision_handler
from maze_handler import maze
from constants import GAME_STARTING, GAME_RUNNING, GAME_LEVEL_UP, GAME_OVER
class UpdateHandler:
    def __init__(self):
        self.frame_counter = 0
    def update(self):
        if HUD_obj.game_state == GAME_STARTING:
            if self.frame_counter <= 90:
                self.frame_counter += 1
            else:
                self.frame_counter = 0
                HUD_obj.game_state = GAME_RUNNING

        elif HUD_obj.game_state == GAME_RUNNING:
            #Check the input of the user
            pacman.change_direction()
            pacman.move()
            blinky.change_direction()
            blinky.change_mode()
            blinky.move()
            colision_handler.pellet_eaten_check()
            #This if updates the logic of the fruit, it is drawn for 300 frames, if it hasn't been eaten in that number of frames, then it counts as eaten but doesn't sum points
            if fruit_object.eaten == False and self.frame_counter <= 300:
                self.frame_counter += 1
                colision_handler.fruit_collision_check()
            else:
                self.frame_counter = 0
                fruit_object.eaten = True
            
            HUD_obj.score_update()

        elif HUD_obj.game_state == GAME_LEVEL_UP:
            #Condition to make the maze blink for 120 frames when pacman has eaten all pellets, and then execute the level up logic 
            if self.frame_counter <= 120:
               self.frame_counter += 1 
            
            else:
                self.frame_counter = 0
                maze.reset()
                colision_handler.reset()
                pacman.reset()
                blinky.reset()
                HUD_obj.increase_level()
                

        elif HUD_obj.game_state == GAME_OVER:
            pass

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

Update_handler = UpdateHandler()