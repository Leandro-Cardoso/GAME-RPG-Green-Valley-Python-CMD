class World():
    '''Generate game world.'''
    def __init__(self, name:str = None, location:str = None) -> None:
        self.name = name
        self.location = location
        self.choices = []
    def set_name(self, name:str) -> None:
        '''Set world name.'''
        self.name = name
    def set_location(self, location:str) -> None:
        '''Set world location.'''
        self.location = location
    def make_choice(self, choice:int) -> None:
        '''Make choice, the choice is a number int.'''
        self.choices.append(choice)

if __name__ == '__main__':
    world = World(location = 'Green Valley')
    print('Location:', world.location)

    world.make_choice(2)
    world.make_choice(4)
    world.make_choice(1)
    print('Choices:', world.choices)
