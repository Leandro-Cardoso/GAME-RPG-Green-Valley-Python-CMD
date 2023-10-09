class Player():
    '''Generate player.'''
    def __init__(self, name:str = None) -> None:
        self.name = name
        self.life = 100
        self.max_life = 100
        self.coins = 0
        self.inventory = []
        self.stats = {
            'strength' : 10,
            'dexterity' : 10,
            'constitution' : 10,
            'intelligence' : 10,
            'wisdom' : 10,
            'charisma' : 10,
            'perception' : 10
        }

    def set_name(self, name:str) -> None:
        '''Change the name of player.'''
        self.name = name
    
    def heal_life(self, heal_points:int) -> None:
        '''Heal X player's life.'''
        if heal_points + self.life > self.max_life:
            self.life = self.max_life
        else:
            self.life += heal_points

    def damage(self, damage_points:int) -> None:
        '''Inflict X damage player's life.'''
        if damage_points > self.life:
            self.life = 0
        else:
            self.life -= damage_points

    def add_coins(self, coins:int) -> None:
        '''Add some coins.'''
        self.coins += coins
        
    def remove_coins(self, coins:int) -> None:
        '''Remove some coins.'''
        self.coins -= coins
