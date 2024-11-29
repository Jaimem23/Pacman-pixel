import pyxel
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
class Maze:
    ''' This class is used to register the walls in the map that has been loaded, and put their positions into a matrix '''

    def __init__ (self):
        #Atribute used to get the current loaded tilemap
        #This matrix contains the tiles of all the walls in the map
        self.wall_tiles= ((1,2),(2,2),(3,2),(5,2),(6,2),(9,2),(10,2),(13,2),(14,2),(16,2),(17,2),(18,2),(19,2),(20,2),(21,2),(24,2),(25,2),
        (1,3),(2,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(17,3),(18,3),(22,3),(23,3),(26,3),(27,3),
        (0,4),(1,4),(2,4),(3,4),(4,4),(10,4),(11,4),(16,4),(19,4),(21,4),(22,4),
        (4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(12,5),(15,5),(16,5),(19,5),(20,5),(23,5),(25,5),(26,5),
        (5,6),(6,6),(7,6),(9,6),(10,6),(16,6),(19,6),(20,6),(21,6),(22,6),(23,6),(25,6),(26,6),
        (1,7),(2,7),(3,7),(4,7),(7,7),(12,7),(15,7),(20,7),(23,7))
        self.wall_tiles= ((1,2),(2,2),(3,2),(5,2),(6,2),(9,2),(10,2),(13,2),(14,2),(16,2),(17,2),(18,2),(19,2),(20,2),(21,2),(24,2),(25,2),
        (1,3),(2,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(17,3),(18,3),(22,3),(23,3),(26,3),(27,3),
        (0,4),(1,4),(2,4),(3,4),(4,4),(10,4),(11,4),(16,4),(19,4),(21,4),(22,4),
        (4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(12,5),(15,5),(16,5),(19,5),(20,5),(23,5),(25,5),(26,5),
        (5,6),(6,6),(7,6),(9,6),(10,6),(16,6),(19,6),(20,6),(21,6),(22,6),(23,6),(25,6),(26,6),
        (1,7),(2,7),(3,7),(4,7),(7,7),(12,7),(15,7),(20,7),(23,7))
        #A new matrix is going to be build to store all of the data of the map (corridors and walls)
        self.map_matrix = []


    def matrix_create(self):
        for y in range(504):
            self.map_matrix.append([])
            for x in range (448):
                #If the tile is in the wall list, a wall (1) is append
                if pyxel.tilemap(0).pget(x,y) in self.wall_tiles:
                    self.map_matrix[y].append(1)
                    #pyxel.rect(x*8, y*8, 8, 8, 3) #Temporary
                #If the tile is not in the wall list, a corridor (0) is appended
                else:
                    self.map_matrix[y].append(0)
                    #pyxel.rect(x*8, y*8, 8, 8,0) #Temporary

maze = Maze()