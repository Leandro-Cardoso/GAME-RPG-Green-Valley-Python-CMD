class World():
    '''Generate game world.'''
    def __init__(self, name:str = None, location:str = None) -> None:
        self.name = name
        self.location = location
        self.choice_ids = []
    def set_name(self, name:str) -> None:
        '''Set world name.'''
        self.name = name
    def set_location(self, location:str) -> None:
        '''Set world location.'''
        self.location = location
    def add_choice_id(self, choice_id:int) -> None:
        '''Add choice id in choice id list.'''
        self.choice_ids.append(choice_id)

if __name__ == '__main__':
    world = World(location = 'Green Valley')
    print('Location:', world.location)

    world.make_choice(2)
    world.make_choice(4)
    world.make_choice(1)
    print('Choices:', world.choices)
