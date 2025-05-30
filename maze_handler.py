import pyxel
from consumable import Consumable

class Maze:
    ''' This class is used to register the elements (maps, pellets, power_pellets), and put their positions into a matrix '''

    def __init__ (self):
        #This matrix contains the tiles of all the walls in the map
        self.wall_tiles= ((0,17),(1,2),(2,2),(3,2),(5,2),(6,2),(9,2),(10,2),(13,2),(14,2),(16,2),(17,2),(18,2),(19,2),(20,2),(21,2),(24,2),(25,2),
        (1,3),(2,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(17,3),(18,3),(22,3),(23,3),(26,3),(27,3),
        (0,4),(1,4),(2,4),(3,4),(4,4),(10,4),(11,4),(16,4),(19,4),(21,4),(22,4),
        (4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(12,5),(15,5),(16,5),(19,5),(20,5),(23,5),(25,5),(26,5),
        (5,6),(6,6),(7,6),(9,6),(10,6),(16,6),(19,6),(20,6),(21,6),(22,6),(23,6),(25,6),(26,6),
        (1,7),(2,7),(3,7),(4,7),(7,7),(12,7),(15,7),(20,7),(23,7))
        #This matrix contains all of the walls of the map for the ghosts
        self.ghost_wall_tiles = ((1,2),(2,2),(3,2),(5,2),(6,2),(9,2),(10,2),(13,2),(14,2),(16,2),(17,2),(18,2),(19,2),(20,2),(21,2),(24,2),(25,2),
        (1,3),(2,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(17,3),(18,3),(22,3),(23,3),(26,3),(27,3),
        (0,4),(1,4),(2,4),(3,4),(4,4),(10,4),(11,4),(16,4),(19,4),(21,4),(22,4),
        (4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(12,5),(15,5),(16,5),(19,5),(20,5),(23,5),(25,5),(26,5),
        (5,6),(6,6),(7,6),(9,6),(10,6),(16,6),(19,6),(20,6),(21,6),(22,6),(23,6),(25,6),(26,6),
        (1,7),(2,7),(3,7),(4,7),(7,7),(12,7),(15,7),(20,7),(23,7))
        #The tilemap position of the pellets
        self.pellet_tile = (5,0)
        self.power_pellet_tile = (7,0)
        #New matrices are going to be build to store all of the data of the map (corridors and walls)
        #One for pacman and another one for ghost
        self.map_matrix = []
        self.ghost_map_matrix = []
        #A list that will be filled later with the pellet objects in the map
        self.pellet_positions = []

    def reset(self):
        '''A function to reset the values when restarting or leveling up'''
        for element in self.pellet_positions:
            element.eaten = False

    def map_matrix_create(self):
        '''A function to create a matrix with the elements of the maze and a list with the pellet positions'''
        for y in range(62):
            self.map_matrix.append([])
            for x in range(62):
                #If the tile is in the wall list, a wall (1) is append
                if pyxel.tilemaps[0].pget(x,y) in self.wall_tiles:
                    self.map_matrix[y].append(1)
                #If the tile is a pellet create a pellet object in the pellet list and append a 0 in map matrix
                elif pyxel.tilemaps[0].pget(x,y) == self.pellet_tile:
                    self.pellet_positions.append(Consumable(x,y, False))
                    self.map_matrix[y].append(0)
                #If the tile is a power pellet, create a power_pellet object and append a 3 (internal number for corridor with power pellet)
                elif pyxel.tilemaps[0].pget(x,y) == self.power_pellet_tile:
                    self.pellet_positions.append(Consumable(x,y, False))
                    self.map_matrix[y].append(3)
                #If the tile is not in the wall list, a corridor (0) is appended
                else:
                    self.map_matrix[y].append(0)

    def create_ghost_map_matrix(self):
        '''A function used to create the matrix with the elements of the map for the ghosts'''
        for y in range(62):
            self.ghost_map_matrix.append([])
            for x in range(62):
                #If the tile is in the wall list, a wall (1) is append
                if pyxel.tilemaps[0].pget(x,y) in self.ghost_wall_tiles:
                    self.ghost_map_matrix[y].append(1)
                #If the tile is not in the wall list, a corridor (0) is appended
                else:
                    self.ghost_map_matrix[y].append(0)

#Create a maze object
maze = Maze()