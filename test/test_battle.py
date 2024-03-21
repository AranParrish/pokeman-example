from src.battle import Battle
from src.pokemon import Pokemon
import pytest

@pytest.fixture
def pikachu():
    return ['Pikachu', 50, 20, 'Headbutt']

@pytest.fixture
def flareon():
    return ["Flareon", 65, 20, "Fire blast"]


@pytest.mark.describe('Attribute Tests')
class TestAttributes:    
    @pytest.mark.it('Has pokemon_1, pokemon_2 and take_turn attributes')
    def test_battle_has_required_attributes(self, pikachu, flareon):
        test_pokemon_1 = Pokemon(*pikachu)
        test_pokemon_2 = Pokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert isinstance(test_battle.pokemon_1, Pokemon)
        assert isinstance(test_battle.pokemon_2, Pokemon)
        assert isinstance(test_battle.current_turn, int)

    @pytest.mark.it('Pokemon instances in Battle are same as those passed to constructor')
    def test_battle_initialises_with_passed_pokemon_instances(self, pikachu, flareon):
        test_pokemon_1 = Pokemon(*pikachu)
        test_pokemon_2 = Pokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert test_battle.pokemon_1 is test_pokemon_1
        assert test_battle.pokemon_2 is test_pokemon_2
    
    @pytest.mark.it('Check current_turn initialises to 1')
    def test_battle_initiliases__current_turn__to_1(self, pikachu, flareon):
        test_pokemon_1 = Pokemon(*pikachu)
        test_pokemon_2 = Pokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert test_battle.current_turn == 1

    