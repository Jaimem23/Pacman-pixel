import pyxel

#This implmenetation is for the map blinking it is not finished yet, IMPORTANT, not final form of UI_Handler
#A limit still needs to be implemented on the blinking of the map
class UIHandler:
    def __init__(self):
        self.Blinking = False
        self.counter = 0
        pyxel.load("assets/pacman_map_blinking.pyxres")
        pyxel.load("assets/pacman_map.pyxres")

    def update(self):
        pyxel.cls(0)
        if self.counter%10 == 0 and not self.Blinking:
            self.Blinking = True
        elif self.counter%10 == 0 and self.Blinking:
            self.Blinking = False
        
    def draw(self):
        if not self.Blinking:
            pyxel.load("assets/pacman_map.pyxres")
            pyxel.bltm(126, 200, 0, 0, 0, 500, 500, None, None, 1.5)
            self.counter += 1
        else:
            pyxel.load("assets/pacman_map_blinking.pyxres")
            pyxel.bltm(126, 200, 0, 0, 0, 500, 500, None, None, 1.5)
            self.counter += 1



#Original code
"""
class App:
    def __init__(self):
        # Initialize Pyxel with a window size of 160x120
        pyxel.init(675, 900, "Pyxel Map Example")
        
        self.Blinking = False
        self.counter = 0
        # Start the game loop
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # Update game logic here (if any)
        pass
    
    def draw(self):
        # Clear the screen
        pyxel.cls(0)
        
        if self.counter%20 == 0 and not self.Blinking:
            self.Blinking = True
        elif self.counter%20 == 0 and self.Blinking:
            self.Blinking = False
        
        # Draw the tilemap
        # Parameters: pyxel.bltm(dest_x, dest_y, tmap, src_x, src_y, width, height)
        if not self.Blinking:
            pyxel.load("assets/pacman_map.pyxres")
            pyxel.bltm(126, 200, 0, 0, 0, 500, 500, None, None, 1.5)
            self.counter += 1
        else:
            pyxel.load("assets/pacman_map_blinking.pyxres")
            pyxel.bltm(126, 200, 0, 0, 0, 500, 500, None, None, 1.5)
            self.counter += 1
            
# Run the app
App()
"""
