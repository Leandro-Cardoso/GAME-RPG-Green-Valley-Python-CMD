import json

from config import GAME_HISTORY_PATH, GAME_HISTORY_NAMES

def find_history(choice_id:list) -> dict:
    '''Find actual history point, based in choice id.'''
    for history_name in GAME_HISTORY_NAMES:
        file_path = GAME_HISTORY_PATH + '\\' + history_name
        with open(file_path, 'r') as json_file:
            history = json.load(json_file)
            json_file.close()
        if history['id'] == choice_id:
            return history

def draw_window() -> None:
    '''Draw game window in CMD.'''
    draw_url = ''
