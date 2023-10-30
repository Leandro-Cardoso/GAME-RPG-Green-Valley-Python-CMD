import json, textwrap
from os import listdir, system

from config import GAME_JSON_PATH, GAME_AUTHOR

class Screen():
    '''Create a screen.'''
    def __init__(self, id:int = 0) -> None:
        self.id = id
        self.game_title = self.get_game_title()
        self.json = self.get_json()
        self.title = self.json['title']
        self.description = self.json['description']
        self.choices = self.json['choices']
        self.choice_ids = self.json['choice_ids']

    def get_game_title(self) -> list:
        '''Get game title from Json file.'''
        file_path = GAME_JSON_PATH + '\\base.json'
        with open(file_path, 'r', encoding = 'utf-8') as file:
            file_json = json.load(file)
            file.close()
        return file_json['game_title']

    def get_json(self) -> dict:
        '''Get Json file by id.'''
        jsons = listdir(GAME_JSON_PATH)
        for file in jsons:
            with open(GAME_JSON_PATH + '\\' + file, 'r', encoding = 'utf-8') as json_file:
                converted_file = json.load(json_file)
                json_file.close()
            if converted_file['id'] == self.id:
                return converted_file
            
    def draw(self) -> None:
        '''Draw game screen.'''
        system('cls')

        # DRAW GAME TITLE:
        print('=' * 100)
        for line in self.game_title:
            print(f'{line:^100}')
        
        # DRAW TITLE:
        if self.title == '':
            title = ''
        else:
            title = ' ' + self.title + ' '
        title = f'\n{title:=^100}\n'
        print(title.upper())

        # DRAW DESCRIPTION:
        if self.description != '':
            print(textwrap.fill(self.description, width = 100))
            print('\n' + '-' * 100 + '\n')
        
        # DRAW CHOICES:
        for i, choice in enumerate(self.choices):
            choice = choice.upper()
            print(f' {i + 1} - {choice}')

        # DRAW AUTHOR:
        author = ' By ' + GAME_AUTHOR['name'] + ' '
        print(f'\n{author:=^100}')
