import pyxel
from item_colision import item_colision
from blinky import blinky
from clyde import clyde
from pinky import pinky
from inky import inky
from maze_handler import maze
from pacman import pacman
from HUD import HUD_obj
from fruit import fruit_object
from constants import GAME_STARTING, GAME_RUNNING, GAME_LEVEL_UP, GAME_OVER 
from ghost_handler import ghost_handler

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
            #Update the status of the ghosts
            ghost_handler.update_ghosts_mode()
            ghost_handler.update_ghosts()
            ghost_handler.activate_blink_mode()
            ghost_handler.check_ghosts_moves()
            #Update the status of pacman according to the user input
            pacman.change_direction()
            pacman.move()
            item_colision.pellet_eaten_check()
            #This if updates the logic of the fruit, it is drawn for 300 frames, if it hasn't been eaten in that number of frames, then it counts as eaten but doesn't sum points
            if fruit_object.eaten == False and self.frame_counter <= 300:
                self.frame_counter += 1
                item_colision.fruit_collision_check()
            else:
                self.frame_counter = 0
                fruit_object.eaten = True
            #Update the high score if the current level score is higher than the highest recorded high score
            HUD_obj.score_update()

        elif HUD_obj.game_state == GAME_LEVEL_UP:
            #Condition to make the maze blink for 120 frames when pacman has eaten all pellets
            if self.frame_counter <= 120:
               self.frame_counter += 1 
            #When the blink has been on screen for 120 frames, reset game parameters to execute the new level
            else:
                self.frame_counter = 0
                self.global_reset()
                

        elif HUD_obj.game_state == GAME_OVER:
            pass

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()

    def global_reset(self):
        '''A function to call all of the reset functions in the game'''
        pacman.reset()
        maze.reset()
        item_colision.reset()
        ghost_handler.reset()
        HUD_obj.increase_level()
        item_colision.reset()


Update_handler = UpdateHandler()