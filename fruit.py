import random
from consumable import Consumable
from constants import FRUIT_X_POS, FRUIT_Y_POS
from HUD import HUD_obj
class Fruit(Consumable):
   '''A class that is a child of Consumable. I contains the logic used to calculate which fruit is going to be spawned,
   its value and is in charge of storing the status of the fruit'''

   def __init__(self, x_pos, y_pos, width, height, eaten, x_pos_tile,y_pos_tile, fruit_number):
      super().__init__(x_pos, y_pos, eaten)
      #Internal naming of the fruits: 1.Cherry 2.Raspberry 3.Orange 4.Apple 5.Watermelon 6.Axe 7.Bell 8.Key
      self.fruit_ID = {"1": (0, 176), "2": (16, 176), "3": (32,176), "4": (48, 176), "5":(64, 176), "5":()} 
      self.fruit_value = {"1": 100, "2": 150, "3": 200, "4": 250, "5":300, "6": 350, "7": 400, "8": 500}
      self.eaten = eaten
      self.width = width
      self.height = height
      self.y_pos_tile = y_pos_tile
      self.x_pos_tile = x_pos_tile
      self.fruit_number = fruit_number
   
   #Read only property
   @property
   def value(self):
      return int(HUD_obj.level * self.fruit_value[str(self.fruit_number)])
   
   @property
   def width(self):
        return self.__widht
    
   @width.setter
   def width(self,widht):
        if not isinstance(widht,int):
            raise TypeError("widht value must be an integer")
        elif widht < 0:
            raise ValueError("Widht must be positive or 0 ")
        self.__widht = widht

   @property
   def height(self):
        return self.__height
    
   @height.setter
   def height(self,height):
        if not isinstance(height,int):
            raise TypeError("Height value must be an integer")
        elif height < 0:
            raise ValueError("Height must be positive or 0 ")
        self.__height = height

       
   def fruit_spawn(self):
      #Choose a random fruit (number) to spawn and update the object parameters
      selected_fruit = random.randint(1,5)
      fruit_object.x_pos_tile = self.fruit_ID[str(selected_fruit)][0]
      fruit_object.y_pos_tile = self.fruit_ID[str(selected_fruit)][1]
      fruit_object.fruit_number = selected_fruit

#Create a fruit object (Cherry by default)
fruit_object = Fruit(FRUIT_X_POS, FRUIT_Y_POS, 16, 16, True, 0, 176,1)
    
