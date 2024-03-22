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
            raise PokemonFaintedException(attacker.name)
        
        defender.take_damage(attacker.get_multiplier(defender)
                             * attacker.attack_damage)
        
        self.current_attacker, self.current_defender = defender, attacker

    def get_winner(self):
        if self.pokemon_1.has_fainted():
            return self.pokemon_2.name
        if self.pokemon_2.has_fainted():
            return self.pokemon_1.name
        
        return None


class PokemonFaintedException(Exception):
    def __init__(self, pokemon_name):
        super().__init__(f'{pokemon_name} has fainted')