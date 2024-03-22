from src.pokemon import Pokemon
from random import randrange

class Battle():
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.current_attacker = pokemon_1
        self.current_defender = pokemon_2

    def take_turn(self, critical_chance=0):
        attacker, defender = self.current_attacker, self.current_defender

        if attacker.has_fainted():
            raise PokemonFaintedException(attacker.name)
        
        damage = attacker.get_multiplier(defender) * attacker.attack_damage

        if (critical := (randrange(0, 10) >= (10*(1-critical_chance)))):
            damage *= 3
        
        defender.take_damage(damage)
        
        self.current_attacker, self.current_defender = defender, attacker

        return_string=''

        if critical:
            return_string += 'CRITICAL HIT! '

        return return_string + f'{attacker.name} used {attacker.move} for {damage} damage!'

    def get_winner(self):
        if self.pokemon_1.has_fainted():
            return self.pokemon_2.name
        if self.pokemon_2.has_fainted():
            return self.pokemon_1.name
 
        return None

    def __str__(self):
        return f"Battle between {self.pokemon_1.name} and {self.pokemon_2.name}"


class PokemonFaintedException(Exception):
    def __init__(self, pokemon_name):
        super().__init__(f'{pokemon_name} has fainted')