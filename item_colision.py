from pacman import pacman
from maze_handler import maze
from fruit import fruit_object
from HUD import HUD_obj
from constants import GAME_LEVEL_UP
from ghost_handler import ghost_handler
class ItemColision():
    def __init__(self):
        self.pellet_positions = maze.pellet_positions
        self.__map_matrix = maze.map_matrix
        self.__eaten_pellets = 0

    def reset(self):
        """A function that resets the pelets"""
        self.__eaten_pellets = 0
        self.pellet_positions = maze.pellet_positions

    def pellet_eaten_check(self):
        '''This function checks if the position pacman is going to has an active pellet in it, if it has, it erases the pellet and sums the value to the score'''
        #Check if there's a pellet in the position and if there is, change the pellet status to eaten
        for element in self.pellet_positions:
            if (element.x_pos >= int(pacman.x_pos/8 + 1) and element.x_pos < int(pacman.x_pos/8 + 3)) and (element.y_pos >= int(pacman.y_pos/8 + 1) and element.y_pos < int(pacman.y_pos/8 + 3)):
                if not element.eaten and self.__map_matrix[element.y_pos][element.x_pos] != 3:
                    element.eaten = True
                    self.__eaten_pellets += 1
                    HUD_obj.current_score += 10
                    self.pellet_status_update()
                elif not element.eaten and self.__map_matrix[element.y_pos][element.x_pos] == 3:
                    element.eaten = True
                    self.__eaten_pellets += 1
                    HUD_obj.current_score += 50
                    ghost_handler.activate_blink_mode()
                    self.pellet_status_update()

    def pellet_status_update(self):
        '''A function that checks if certain conditions of pellets are met and change the game execution'''
    #Check if the fruit has been eaten (is not on screen) and change the parameters to make ir appear
        if (self.__eaten_pellets == 70 or self.__eaten_pellets == 170) and fruit_object.eaten:
            fruit_object.fruit_spawn()
            fruit_object.eaten = False

    #If Pacman has eaten all of the pellets, the game ends
        if len(self.pellet_positions) == self.__eaten_pellets:
            #Select the required sprite for pacman on the victory screen according to the direction
            if pacman.direction.lower() == "up":
                pacman.x_pos_tile = 16
                pacman.y_pos_tile = 32
            elif pacman.direction.lower() == "down":
                pacman.x_pos_tile = 16
                pacman.y_pos_tile = 48
            elif pacman.direction.lower() == "right":
                pacman.x_pos_tile = 16
                pacman.y_pos_tile = 0
            elif pacman.direction.lower() == "left":
                pacman.x_pos_tile = 16
                pacman.y_pos_tile = 16
            #Change the direction by stand-by and set the game has ended
            pacman.direction = "stand-by"
            HUD_obj.game_state = GAME_LEVEL_UP

    def fruit_collision_check(self):
        '''A function that checks if Pacman collides with the fruit'''
        if ( 26 >= int(pacman.x_pos/8 + 1) and 26 < int(pacman.x_pos/8 + 2)) and (33 == int(pacman.y_pos/8)):
                fruit_object.eaten = True
                HUD_obj.current_score += fruit_object.value

    def power_pellet_activate(self):
        '''A function that activates the frightened mode of the ghosts if a power pellet is eaten'''
        ghost_handler.activate_blink_mode()

item_colision = ItemColision()