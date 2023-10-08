import sys, json

# CONFIS:
from config import GAME_PATH

sys.path.insert(0, GAME_PATH)

from game.models import *

world = World()
player = Player()

# DRAW WINDOW:
def draw_window() -> None:
    '''Draw game window in CMD'''
    draw_url = ''

if __name__ == '__main__':
    d20 = Dice(20)

    player.set_name('Leandro')

    print(player.name, d20.roll())
    print('AQUI >>>', GAME_PATH)
