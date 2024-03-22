from src.pokemon import Pokemon, FirePokemon, GrassPokemon, WaterPokemon, NormalPokemon
from src.pokeball import Pokeball, PokeballFullException
import pytest, types

@pytest.fixture
def pikachu():
    return ['Pikachu', 50, 20, 'Lightning bolt']

@pytest.fixture
def flareon():
    return ["Flareon", 65, 20, "Fire blast"]

@pytest.fixture
def leafeon():
    return ["Leafeon", 65, 17, "Giga drain"]

@pytest.fixture
def vaporeon():
    return ["Vaporeon", 70, 19, "Hydro pump"]

@pytest.fixture
def eevee():
    return ["Eevee", 55, 18, "Headbutt"]


@pytest.mark.describe('Tests for Pokeball class')
class TestPokeball:
    def test_pokeball_initialises_with_no_current_pokemon(self):
        test_pokeball = Pokeball()

        assert test_pokeball.current_pokemon == None

    def test_pokeball_has_catch_method(self):
        test_pokeball = Pokeball()

        assert isinstance(test_pokeball.catch, types.MethodType)

    def test_pokeball_catch_method_captures_pokemon(self, pikachu):
        test_pikachu = NormalPokemon(*pikachu)
        test_pokeball = Pokeball()

        test_pokeball.catch(test_pikachu)

        assert test_pokeball.current_pokemon is test_pikachu

    def test_pokeball_raises_exception_when_catch_called_with_pokeball_filled(self, pikachu):
        test_pikachu_1 = NormalPokemon(*pikachu)
        test_pikachu_2 = NormalPokemon(*pikachu)
        test_pokeball = Pokeball()

        test_pokeball.catch(test_pikachu_1)

        with pytest.raises(PokeballFullException) as exc_info:
            test_pokeball.catch(test_pikachu_2)

        assert "Pokeball already contains pokemon" in str(exc_info.value)

    def test_pokeball_has__is_empty__method(self):
        test_pokeball = Pokeball()

        assert isinstance(test_pokeball.is_empty, types.MethodType)

    def test_pokeball__is_empty__method_returns_boolean(self):
        test_pokeball = Pokeball()

        assert isinstance(test_pokeball.is_empty(), bool)
    
    def test_pokeball__is_empty__returns_true_when_pokeball_empty(self):
        test_pokeball = Pokeball()

        assert test_pokeball.is_empty()

    def test_pokeball__is_empty__returns_false_when_pokeball_contains_pokemon(self, pikachu):
        test_pokemon = NormalPokemon(*pikachu)
        test_pokeball = Pokeball()
        test_pokeball.catch(test_pokemon)

        assert test_pokeball.is_empty() is False

    def test_pokeball__returns_expected_message_when_empty(self):
        test_pokeball = Pokeball()

        assert str(test_pokeball) == "Empty pokeball"

    def test_pokeball__returns_stored_pokemon_name_when_filled(self, pikachu):
        test_pokemon = NormalPokemon(*pikachu)
        test_pokeball = Pokeball()
        test_pokeball.catch(test_pokemon)

        assert str(test_pokeball) == "Pokeball containing Pikachu"