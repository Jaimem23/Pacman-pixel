import pyxel
from item_colision import item_colision
from maze_handler import maze
from pacman import pacman
from HUD import HUD_obj
from fruit import fruit_object
from constants import GAME_STARTING, GAME_RUNNING, GAME_LEVEL_UP, GAME_OVER, GAME_LIVE_LOST
from ghost_handler import ghost_handler

class UpdateHandler:
    def __init__(self):
        self.frame_counter = 0
        self.fruit_frame_counter = 0

    def update(self):
        if HUD_obj.game_state == GAME_STARTING:
            if self.frame_counter <= 90:
                self.frame_counter += 1
            else:
                self.frame_counter = 0
                HUD_obj.game_state = GAME_RUNNING

        elif HUD_obj.game_state == GAME_RUNNING:
            #Update the status of the ghosts
            ghost_handler.update_ghosts()
            #Update the status of pacman according to the user input
            pacman.change_direction()
            pacman.move()
            item_colision.pellet_eaten_check()
            #This if updates the logic of the fruit, it is drawn for 300 frames, if it hasn't been eaten in that number of frames, then it counts as eaten but doesn't sum points
            if fruit_object.eaten == False and self.fruit_frame_counter <= 300:
                self.fruit_frame_counter += 1
                item_colision.fruit_collision_check()
            else:
                self.fruit_frame_counter = 0
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
                HUD_obj.increase_level()
                self.global_reset()
                
        elif HUD_obj.game_state == GAME_LIVE_LOST:
            #A condition to restart the game when Pacman has died and reset the game if pacman has lives left, otherwise display game over screen
            if self.frame_counter <= 60:
               self.frame_counter += 1 
            #When pacman finishes the death screen (120 frames) and the continue count has been completed (90 frames)
            #The game starts running again if pacman still has lives, otherwise game over is displayed
            elif pacman.lives != 0:
                self.frame_counter = 0
                self.fruit_frame_counter = 0
                pacman.reset()
                ghost_handler.reset()
                HUD_obj.game_state = GAME_STARTING

            else:
                self.frame_counter = 0
                HUD_obj.game_state = GAME_OVER
        
        elif HUD_obj.game_state == GAME_OVER:
            #A condition to display the game over screen till S is pressed
            if(pyxel.btn(pyxel.KEY_S)):
                self.global_reset()
                HUD_obj.current_score = 0
                HUD_obj.level = 1
                pacman.lives = 3
                HUD_obj.game_state = GAME_STARTING

        if(pyxel.btn(pyxel.KEY_ESCAPE)):
            pyxel.quit()


    def global_reset(self):
        '''A function to call all of the reset functions in the game'''
        pacman.reset()
        maze.reset()
        item_colision.reset()
        ghost_handler.reset()


Update_handler = UpdateHandler()