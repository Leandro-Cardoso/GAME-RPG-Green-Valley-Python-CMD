import json, textwrap

from config import GAME_HISTORY_PATH, GAME_HISTORY_NAMES

class World():
    '''Generate game world.'''
    def __init__(self, name:str = None, location:str = None) -> None:
        self.name = name
        self.location = location
        self.choice_ids = [1000]
        self.history = None
        self.find_history()

    def set_name(self, name:str) -> None:
        '''Set world name.'''
        self.name = name

    def set_location(self, location:str) -> None:
        '''Set world location.'''
        self.location = location

    def add_choice_id(self, choice_id:int) -> None:
        '''Add choice id in choice id list.'''
        self.choice_ids.append(choice_id)

    def find_history(self) -> None:
        '''Find actual history point, based in choice id.'''
        for history_name in GAME_HISTORY_NAMES:
            file_path = GAME_HISTORY_PATH + '\\' + history_name

            with open(file_path, 'r', encoding = 'utf-8') as json_file:
                history_to_check = json.load(json_file)
                json_file.close()

            if history_to_check['id'] == self.choice_ids[-1]:
                self.history = history_to_check
                break

    def draw_window(self) -> None:
        '''Draw game window in CMD.'''
        chapter_number = self.history['chapter_number']
        chapter_name = self.history['chapter_name']
        chapter = f' CAPÍTULO {chapter_number}: {chapter_name} '
        print(f'{chapter:=^100}\n')

        text = self.history['description']
        print(textwrap.fill(text, width = 100))
