from UI_handler import  UI_Handler
import pyxel
from update_handler import Update_handler
class App():
    '''The main class of the app, it is in charge of executing the Update and Ui_handler classes'''
    def __init__(self) -> None:
        pyxel.run(Update_handler.update,UI_Handler.draw)

App()