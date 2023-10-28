import sys

# GAME CONFIGS:
from config import *
for path in GAME_PATHS:
    sys.path.insert(0, path)

# CREATE GAME OBJECTS:
from game import Game
game = Game()

# RUN:
game.run()
