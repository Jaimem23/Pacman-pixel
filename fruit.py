import random
from consumable import Consumable
from constants import FRUIT_X_POS, FRUIT_Y_POS
from HUD import HUD_obj
class Fruit(Consumable):
   def __init__(self, x_pos, y_pos, widht, height, eaten, x_pos_tile,y_pos_tile, fruit_number):
      super().__init__(x_pos, y_pos, widht, height, eaten)
      self.fruit_ID = {"1": (0, 176), "2": (16, 176), "3": (32,176), "4": (48, 176), "5":(64, 176)} #Internal naming of the fruits: 1.Cherry 2.Raspberry 3.Orange 4.Apple 5.Watermelon
      self.fruit_value = {"1": 100, "2": 150, "3": 200, "4": 250, "5":500}
      self.fruit_number = fruit_number
      self.y_pos_tile = y_pos_tile
      self.x_pos_tile = x_pos_tile
      self.cycle_counter = 0
   
   #Read only property
   @property
   def value(self):
      return int(HUD_obj.level) * self.fruit_value[str(self.fruit_number)]

   def fruit_update(self):
      '''A function to update the number of cycles that the fruit has been on screen'''
      self.cycle_counter += 1
   
          
   def fruit_spawn(self):
      #Choose a random fruit (number) to spawn and update the object parameters
      selected_fruit = random.randint(1,5)
      fruit_object.x_pos_tile = self.fruit_ID[str(selected_fruit)][0]
      fruit_object.y_pos_tile = self.fruit_ID[str(selected_fruit)][1]
      fruit_object.fruit_number = selected_fruit

#Create a fruit object (Cherry by default)
fruit_object = Fruit(FRUIT_X_POS, FRUIT_Y_POS, 16, 16, False, 0, 176,1)
    
