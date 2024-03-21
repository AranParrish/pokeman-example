from src.pokemon import Pokemon

class Battle():
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.current_turn = 0

        self.pokemon_1_damage = (pokemon_1.get_multiplier(pokemon_2) 
                                 * pokemon_1.attack_damage)
        self.pokemon_2_damage = (pokemon_2.get_multiplier(pokemon_1)
                                 * pokemon_2.attack_damage)

    def take_turn(self):
        if self.current_turn == 0:
            attacker = self.pokemon_1
            defender = self.pokemon_2
        else:
            attacker = self.pokemon_2
            defender = self.pokemon_1

        if attacker.has_fainted():
            raise Exception(f'{attacker.name} has already fainted')
        
        defender.take_damage(attacker.get_multiplier(defender)
                             * attacker.attack_damage)
        
        self.current_turn = (self.current_turn + 1) % 2