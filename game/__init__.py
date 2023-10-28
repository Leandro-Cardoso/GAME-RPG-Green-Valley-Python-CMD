import sys

# GAME CONFIGS:
from config import GAME_PATHS
for path in GAME_PATHS:
    sys.path.insert(0, path)

# CREATE GAME OBJECTS:
from game import Game
game = Game()

# RUN:
def run():
    '''Run game.'''
    pass

# TESTS:
if __name__ == '__main__':
    print(game.name)
