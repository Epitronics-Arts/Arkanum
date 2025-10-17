from ursina import *
from scenes.menu import Menu
from scenes.game import Game


app = Ursina()


def start_game():
    print("hello")
    menu.disable()
    game=Game()
    game.enable()

menu = Menu(start_callback=start_game)

app.run()