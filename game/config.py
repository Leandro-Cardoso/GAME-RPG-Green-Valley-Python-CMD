import os

# GAME NAME:
GAME_NAME = 'GREEN VALLEY'

# GAME VERSION:
GAME_VERSION = '0.1.0a'

# GAME REPOSITORY:
GAME_REPOSITORY = 'https://github.com/Leandro-Cardoso/GAME-RPG-Green-Valley-Python-CMD/'

# GAME AUTHORS:
GAME_AUTHORS = {
    'Leandro Cardoso' : {
        'works' : ['core'],
        'github' : 'https://github.com/Leandro-Cardoso'
    }
}

GAME_AUTHORS_STR = 'Desenvolvido por '
for author in GAME_AUTHORS:
    GAME_AUTHORS_STR += author
    if len(GAME_AUTHORS) > 2 and list(GAME_AUTHORS)[-2] == author:
        GAME_AUTHORS_STR += ' e '
    elif list(GAME_AUTHORS)[-1] != author:
        GAME_AUTHORS_STR += ', '
GAME_AUTHORS_STR += '.'

# GAME DESCRIPTION:
GAME_DESCRIPTION = f'{GAME_NAME} (versão {GAME_VERSION}): É um jogo de RPG de texto no tema medieval de fantasia, de mecânica inspirada em "D&D" e "Final Fantasy", desenvolvido para rodar no "CMD do Windows".\nA história se passa na pequena região de "Green Valley". O jogo conta apena uma breve história de uma lore muito mais rica e original e que será explorada em futuros jogos, acompanhe em: {GAME_REPOSITORY}.\n{GAME_AUTHORS_STR}'

# GAME PATH:
GAME_PATH = os.getcwd()

# GAME HISTORY JSONS:
GAME_HISTORY_PATH = GAME_PATH + '\game\history'
GAME_HISTORY_NAMES = os.listdir(GAME_HISTORY_PATH)

# TESTS:
if __name__ == '__main__':
    print(GAME_DESCRIPTION)
