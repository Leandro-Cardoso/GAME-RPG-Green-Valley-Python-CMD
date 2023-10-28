from os import system

class Screen():
    '''Create a screen.'''
    def __init__(self) -> None:
        self.name = ''
    
    def draw_main_menu(self) -> None:
        '''Open game menu.'''
        system('cls')
        title = [
            '=' * 100,
            ' '*3 + '____   ____    _____   _____   _   _    __     __     _      _       _       _____  __   __',
            ' '*2 + '/ ___| |  _ \  | ____| | ____| | \ | |   \ \   / /    / \    | |     | |     | ____| \ \ / /',
            '| |  _  | |_) | |  _|   |  _|   |  \| |    \ \ / /    / _ \   | |     | |     |  _|    \ V /',
            '| |_| | |  _ <  | |___  | |___  | |\  |     \ V /    / ___ \  | |___  | |___  | |___    | |',
            '\____| |_| \_\ |_____| |_____| |_| \_|      \_/    /_/   \_\ |_____| |_____| |_____|   |_|',
            '\0',
            '=' * 100
        ]
        for line in title:
            print(f'{line:^100}')
        
        menu = [
            '1 - Start Game',
            '2 - Credits',
            '3 - Exit Game'
        ]
        print('\0')
        for iten in menu:
            print(f' {iten}')
        
        text = ' By Leandro Cardoso '
        print(f'\n{text:=^100}')

# TESTS:
if __name__ == '__main__':
    screen = Screen()
    screen.open_menu()
