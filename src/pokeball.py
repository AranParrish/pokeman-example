# from src.pokemon import *


class Pokeball():
    def __init__(self):
        self.__current_pokemon = None

    def catch(self, pokemon):
        if self.__current_pokemon:
            raise PokeballFullException
        
        self.__current_pokemon = pokemon

    @property
    def current_pokemon(self):
        return self.__current_pokemon
    
    def is_empty(self):
        return not self.__current_pokemon


class PokeballFullException(Exception):
    def __init__(self):
        super().__init__('Pokeball already contains pokemon')