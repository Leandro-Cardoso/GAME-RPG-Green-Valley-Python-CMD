from os import getcwd

# GAME NAME:
GAME_NAME = 'GREEN VALLEY'

# GAME VERSION:
GAME_VERSION = '0.1.0a'

# GAME REPOSITORY:
GAME_REPOSITORY = 'https://github.com/Leandro-Cardoso/GAME-RPG-Green-Valley-Python-CMD/'

# GAME AUTHOR:
GAME_AUTHOR = {
    'name' : 'Leandro Cardoso',
    'works' : ['core'],
    'github' : 'https://github.com/Leandro-Cardoso'
}

# GAME DESCRIPTION:
GAME_DESCRIPTION = f'{GAME_NAME} (versão {GAME_VERSION}): É um jogo de RPG de texto no tema medieval de fantasia, de mecânica inspirada em "D&D" e "Final Fantasy", desenvolvido para rodar no "CMD do Windows".\nA história se passa na pequena região de "Green Valley". O jogo conta apena uma breve história de uma lore muito mais rica e original e que será explorada em futuros jogos, acompanhe em: {GAME_REPOSITORY}.'

# GAME PATHS:
GAME_ROOT = getcwd()
GAME_PATHS = [
    GAME_ROOT + '\\game\\models'
]

# GAME JSON PATH:
GAME_JSON_PATH = GAME_ROOT + '\\game\\assets'
