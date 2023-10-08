from random import randint

class Dice():
    '''Generate a dice with X faces. Default 6 faces.'''
    def __init__(self, faces:int = 6) -> None:
        self.faces = faces
        self.last_result = 0
    def set_faces(self, faces:int) -> None:
        '''Set number of faces.'''
        self.faces = faces
        self.last_result = 0
    def roll(self) -> int:
        '''Roll the dice, return a random int number.'''
        self.last_result = randint(1, self.faces)
        return self.last_result

if __name__ == '__main__':
    d3 = Dice(3)
    for i in range(0, 10):
        print('D3 =', d3.roll())
