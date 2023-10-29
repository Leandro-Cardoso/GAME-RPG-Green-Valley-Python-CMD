import json, textwrap
from os import listdir, system

from config import GAME_JSON_PATH, GAME_AUTHOR

class Screen():
    '''Create a screen.'''
    def __init__(self, id:int = 1) -> None:
        self.id = id

    def get_dict_by_id(self) -> dict:
        '''Get dict (Json file) by id.'''
        jsons = listdir(GAME_JSON_PATH)
        for file in jsons:
            with open(GAME_JSON_PATH + '\\' + file, 'r', encoding = 'utf-8') as json_file:
                converted_file = json.load(json_file)
                json_file.close()
            if converted_file['id'] == self.id:
                return converted_file
            
    def get_choice_ids(self) -> list:
        '''Get choice ids.'''
        dictionary = self.get_dict_by_id()
        return dictionary['choice_ids']

    def draw(self) -> None:
        '''Draw game screen.'''
        system('cls')
        dictionary = self.get_dict_by_id()

        # DRAW BASE:
        print('=' * 100)
        with open(GAME_JSON_PATH + '\\base.json', 'r', encoding = 'utf-8') as file:
            file_json = json.load(file)
            game_title = file_json['game_title']
            file.close()

        # DRAW GAME TITLE:
        for line in game_title:
            print(f'{line:^100}')
        
        # DRAW TITLE:
        title = ' ' + dictionary['title'] + ' '
        title = f'\n{title:=^100}\n'
        print(title.upper())

        # DRAW DESCRIPTION:
        description = dictionary['description']
        if description != '':
            print(textwrap.fill(description, width = 100))
            print('\n' + '-' * 100 + '\n')
        
        # DRAW OPTIONS:
        options = dictionary['options']
        for i, option in enumerate(options):
            option = option.upper()
            print(f' {i + 1} - {option}')

        # DRAW AUTHOR:
        author = ' By ' + GAME_AUTHOR['name'] + ' '
        author = f'\n{author:=^100}'
        print(author)
