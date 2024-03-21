from src.pokeball import Pokeball
from src.pokemon import *

class Trainer():
    def __init__(self):
        self.belt = [Pokeball() for i in range(6)]

    def throw_pokeball(self, pokemon):
        for pokeball in self.belt:
            if pokeball.is_empty():
                pokeball.catch(pokemon)
                return
        raise Exception('All pokeballs full')