import json, os, textwrap

from config import GAME_HISTORY_PATH, GAME_HISTORY_NAMES

class World():
    '''Generate game world.'''
    def __init__(self, name:str = None, location:str = None) -> None:
        self.name = name
        self.location = location
        self.choiced_ids = [1000]
        self.history = self.get_history(1000)

    def set_name(self, name:str) -> None:
        '''Set world name.'''
        self.name = name

    def set_location(self, location:str) -> None:
        '''Set world location.'''
        self.location = location

    def add_choice_id(self, choice_id:int) -> None:
        '''Add choice id in choice id list.'''
        self.choiced_ids.append(choice_id)

    def draw_menu(self) -> None:
        '''Draw game main menu.'''
        os.system('cls')

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

    def get_history(self, id:int) -> dict:
        '''Get history point, based in id.'''
        for history_name in GAME_HISTORY_NAMES:
            file_path = GAME_HISTORY_PATH + '\\' + history_name

            with open(file_path, 'r', encoding = 'utf-8') as json_file:
                history_to_check = json.load(json_file)
                json_file.close()

            if history_to_check['id'] == id:
                return history_to_check

    def set_history(self, id:int) -> None:
        '''Set actual history point, based in id.'''
        self.history = self.get_history(id)

    def draw_window(self) -> None:
        '''Draw game window in CMD.'''
        os.system('cls')

        chapter_number = self.history['chapter_number']
        chapter_name = self.history['chapter_name']
        text = f' CAPÍTULO {chapter_number}: {chapter_name} '
        print(f'{text:=^100}\n')

        text = self.history['description']
        print(textwrap.fill(text, width = 100))

        text = ''
        print(f'{text:_^100}\n')

        for i, id in enumerate(self.history['choice_ids']):
            history = self.get_history(id)
            option = history['title']
            text = f' {i + 1} - {option}\n'
            print(textwrap.fill(text, width = 100))
        
        text = ' By Leandro Cardoso '
        print(f'\n{text:=^100}')
