import sys

# GAME CONFIGS:
from config import GAME_PATH

sys.path.insert(0, GAME_PATH)

# IMPORTS AND CREATE GAME OBJECTS:
from game.models import *

world = World()
player = Player()

# TESTS:
if __name__ == '__main__':
    d20 = Dice(20)

    player.set_name('Leandro')

    print(player.name, d20.roll())
    world.draw_window()
