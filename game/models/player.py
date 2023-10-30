class Player():
    '''Create player.'''
    def __init__(self, name:str = None) -> None:
        self.name = name
        self.life = 100
        self.max_life = 100
        self.coins = 0
        self.inventory = []
        self.base_stats = {
            'strength' : 10,
            'dexterity' : 10,
            'constitution' : 10,
            'intelligence' : 10,
            'wisdom' : 10,
            'charisma' : 10
        }
        self.stats = self.base_stats
        self.effects = []
        self.effects_stats = {
            'tired' : {
                'strength' : 0.75,
                'dexterity' : 0.75,
                'constitution' : 0.75,
                'intelligence' : 0.75
            }
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
    
    def restaure_stats(self) -> None:
        '''Restaure all player stats.'''
        self.stats = self.base_stats
    
    def apply_effects(self, add_effects:list = [], remove_effects:list = []) -> None:
        '''Add effects to player stats.'''
        self.restaure_stats()

        # ADD EFFECTS:
        for effect in add_effects:
            if effect not in self.effects:
                self.effects.append(effect)
                for stat in list(self.effects_stats[effect]):
                    self.stats[stat] *= self.effects_stats[effect][stat]

        # REMOVE EFFECTS:
        for effect in remove_effects:
            if effect in self.effects:
                self.effects.remove(effect)
