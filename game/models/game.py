from screen import Screen
from player import Player

class Game():
    '''New game.'''
    def __init__(self) -> None:
        self.is_running = False

        self.screen = Screen()
        self.player = Player()
        self.choiced_ids = [1000]

    def open_menu(self) -> int:
        '''Open game menu.'''
        is_open = True
        menu = Screen()
        while is_open:
            pass

    def run(self) -> None:
        '''Run game.'''
        self.is_running = True
        screen = Screen()
        screen.draw()
        #while self.is_running:
            #response = self.open_menu()

    def add_choice_id(self, choice_id:int) -> None:
        '''Add choice id in choice id list.'''
        self.choiced_ids.append(choice_id)
