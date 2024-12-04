from UI_handler import  UI_Handler
import pyxel
from update_handler import Update_handler
class App():
    def __init__(self) -> None:
        pyxel.run(Update_handler.update,UI_Handler.draw)

App()