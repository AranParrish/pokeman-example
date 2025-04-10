from src.pokeball import Pokeball, PokeballFullException
from src.pokemon import *


class AllPokeballsFull(Exception):
    def __init__(self):
        super().__init__("All pokeballs full")


class Trainer:
    def __init__(self, name=""):
        self.belt = [Pokeball() for i in range(6)]
        self.name = name

    def __str__(self):
        return f"Pokemon trainer: {self.name}"

    def throw_pokeball(self, pokemon):
        for i, pokeball in enumerate(self.belt):
            try:
                pokeball.catch(pokemon)
            except PokeballFullException:
                if i == 5:
                    raise AllPokeballsFull
            else:
                break
