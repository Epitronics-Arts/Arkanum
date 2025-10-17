from ursina import *

class Menu(Entity):
    def __init__(self, start_callback):
        super().__init__()
        Text(parent=self,text='Menu Principal', scale=10, y=2)
        Button(parent=self ,text='Jouer', scale=3, y=0, on_click=start_callback)