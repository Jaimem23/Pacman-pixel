from pacman import pacman
from maze_handler import maze
from fruit import fruit_object
class ColisionHandler():
    def __init__(self):
        self.pellet_positions = maze.pellet_positions
        self.__eaten_pellets = 0

    def pellet_eaten_check(self):
        '''This function checks if the position pacman is going to has an active pellet in it, if it has, it erases the pellet and sums the value to the score'''
        #Check if there's a pellet in the position and if there is, change the pellet status to eaten
        for element in self.pellet_positions:
            if (element.x_pos >= int(pacman.x_pos/8 + 1) and element.x_pos < int(pacman.x_pos/8 + 3)) and (element.y_pos >= int(pacman.y_pos/8 + 1) and element.y_pos < int(pacman.y_pos/8 + 3)):
                if not element.eaten and self.__map_matrix[element.y_pos][element.x_pos] != 3:
                    element.eaten = True
                    self.__eaten_pellets += 1
                    self.score += 10
                    self.pellet_status_update()
                elif not element.eaten:
                    element.eaten = True
                    self.__eaten_pellets += 1
                    pacman.score += 500
                    self.pellet_status_update()

    def pellet_status_update(self):
        '''A function that checks if certain conditions of pellets are met and change the game execution'''
    #Check if the conditions to spawn fruit are met
        if (self.__eaten_pellets == 70 or self.__eaten_pellets == 170) and not self.fruit_spawned:
            fruit_object.fruit_spawn()
            self.fruit_spawned = True

    #If Pacman has eaten all of the pellets, the game ends
        if len(self.pellet_positions) == self.__eaten_pellets:
            #Select the required sprite for pacman on the victory screen according to the direction
            if self.direction.lower() == "up":
                self.x_pos_tile = 16
                self.y_pos_tile = 32
            elif self.direction.lower() == "down":
                self.x_pos_tile = 16
                self.y_pos_tile = 48
            elif self.direction.lower() == "right":
                self.x_pos_tile = 16
                self.y_pos_tile = 0
            elif self.direction.lower() == "left":
                self.x_pos_tile = 16
                self.y_pos_tile = 16
            #Change the direction by stand-by and set the game has ended
            self.direction = "stand-by"
            self.game_end = True

    

colision_handler = ColisionHandler()