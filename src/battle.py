from src.pokemon import Pokemon

class Battle():
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.current_attacker = pokemon_1
        self.current_defender = pokemon_2

    def take_turn(self):
        attacker, defender = self.current_attacker, self.current_defender

        if attacker.has_fainted():
            raise Exception(f'{attacker.name} has already fainted')
        
        defender.take_damage(attacker.get_multiplier(defender)
                             * attacker.attack_damage)
        
        self.current_attacker, self.current_defender = defender, attacker