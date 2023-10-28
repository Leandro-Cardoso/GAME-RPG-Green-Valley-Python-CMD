from config import GAME_NAME, GAME_VERSION, GAME_DESCRIPTION
from screen import Screen
from player import Player

class Game():
    '''New game.'''
    def __init__(self) -> None:
        self.name = GAME_NAME
        self.version = GAME_VERSION
        self.description = GAME_DESCRIPTION

        self.screen = Screen()
        self.player = Player()
        self.choiced_ids = [1000]

    def add_choice_id(self, choice_id:int) -> None:
        '''Add choice id in choice id list.'''
        self.choiced_ids.append(choice_id)
    
    def run(self):
        '''Run game.'''
        self.screen.draw_main_menu()
