from sprite import Sprite

class Ghost(Sprite):
    def __init__(self, x_pos, y_pos, widht, height, image):
        super().__init__(x_pos, y_pos, widht, height, image)