import os

# GAME PATH:
GAME_PATH = os.getcwd()

# GAME HISTORY JSONS:
GAME_HISTORY_PATH = GAME_PATH + '\game\history'
GAME_HISTORY_NAMES = os.listdir(GAME_HISTORY_PATH)

if __name__ == '__main__':
    print(GAME_HISTORY_PATH)
    print(GAME_HISTORY_NAMES)
