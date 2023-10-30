from screen import Screen

class Game():
    '''New game.'''
    def __init__(self) -> None:
        self.is_running = False
        self.screen = Screen()
        self.error = ''
        self.choiced_id = 0
        self.choiced_ids = [1000]
    
    def dialogue(self) -> None:
        '''Start dialogue with player.'''
        try:
            response = int(input('DIGITE UMA OPÇÃO: '))
            if response <= len(self.screen.choice_ids):
                self.choiced_id = self.screen.choice_ids[response - 1]
            
            # EXIT:
            elif response == 9:
                self.choiced_id = response

            # ERRORS:
            else:
                self.error = f'A opção {response} não existe, tente outra.'
        except:
            self.error = 'Você precisa digitar um número inteiro.'
    
    def create_screen(self) -> None:
        '''Create screen with player response.'''
        self.screen = Screen(self.choiced_id)
    
    def run(self) -> None:
        '''Run game.'''
        self.is_running = True
        while self.is_running:
            # DRAW SCREEN:
            self.screen.draw()

            # DRAW ERROR:
            if self.error != '':
                print(f'ERRO: {self.error}')

            # START DIALOGUE:
            self.dialogue()

            # EXIT:
            if self.choiced_id == 9:
                self.is_running = False
            
            # CREATE SCREEN:
            else:
                self.create_screen()
