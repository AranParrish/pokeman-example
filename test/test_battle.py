from src.battle import Battle
from src.pokemon import *
import pytest, types

@pytest.fixture
def pikachu():
    return ['Pikachu', 50, 20, 'Headbutt']

@pytest.fixture
def flareon():
    return ["Flareon", 65, 20, "Fire blast"]

@pytest.fixture
def leafeon():
    return ["Leafeon", 65, 17, "Giga drain"]

@pytest.fixture
def vaporeon():
    return ["Vaporeon", 70, 19, "Hydro pump"]


@pytest.mark.describe('Attribute Tests')
class TestAttributes:    
    @pytest.mark.it('Has pokemon_1, pokemon_2 and take_turn attributes')
    def test_battle_has_required_attributes(self, pikachu, flareon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert isinstance(test_battle.pokemon_1, NormalPokemon)
        assert isinstance(test_battle.pokemon_2, FirePokemon)
        assert isinstance(test_battle.current_attacker, NormalPokemon)
        assert isinstance(test_battle.current_defender, FirePokemon)

    @pytest.mark.it('Pokemon instances in Battle are same as those passed to constructor')
    def test_battle_initialises_with_passed_pokemon_instances(self, pikachu, flareon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert test_battle.pokemon_1 is test_pokemon_1
        assert test_battle.pokemon_2 is test_pokemon_2
    
    @pytest.mark.it('Check current attacker initialises to pokemon 1')
    def test_battle_initiliases__current_attacker__to_first_pokemon(self, pikachu, flareon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert test_battle.current_attacker is test_pokemon_1


@pytest.mark.describe('take_turn Method Tests')
class TestTakeTurn:
    @pytest.mark.it('take_turn is a method')
    def test_battle_has__take_turn__method(self, pikachu, flareon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        assert isinstance(test_battle.take_turn, types.MethodType)

    @pytest.mark.it('Pokemon 1 deals damage to pokemon 2 with take_turn')
    def test_battle__take_turn__deals_damage(self, pikachu, flareon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        test_battle.take_turn()

        assert test_pokemon_2.hit_points == 45

    @pytest.mark.it('Pokemon 2 hit points changes after pokemon 1 takes turn')
    def test_battle__take_turn__changes_value_of_hit_points(self, pikachu, flareon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        pokemon_2_initial_hit_points = test_pokemon_2.hit_points

        test_battle.take_turn()

        assert test_pokemon_2.hit_points < pokemon_2_initial_hit_points

    @pytest.mark.it('Pokemon 1 deals different damage to pokemon 2 with different combination of pokemon')
    def test_battle__take_turn__deals_different_damage(self, leafeon, vaporeon):
        test_pokemon_1 = GrassPokemon(*leafeon)
        test_pokemon_2 = WaterPokemon(*vaporeon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        test_battle.take_turn()

        assert test_pokemon_2.hit_points == 44.5

    @pytest.mark.it('Current attacker changes after turn has been taken')
    def test_battle__current_attacker__attribute_is_updated_after__take_turn__called(self, leafeon, vaporeon):
        test_pokemon_1 = GrassPokemon(*leafeon)
        test_pokemon_2 = WaterPokemon(*vaporeon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        test_battle.take_turn()

        assert test_battle.current_attacker is test_pokemon_2

    @pytest.mark.it('Current turn reverts to Pokemon 1 after two turns taken')
    def test_battle__current_turn__attribute_switches_back_to_0_after__take_turn__called_twice(self, leafeon, vaporeon):
        test_pokemon_1 = GrassPokemon(*leafeon)
        test_pokemon_2 = WaterPokemon(*vaporeon)
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        test_battle.take_turn()
        test_battle.take_turn()

        assert test_battle.current_attacker is test_pokemon_1

    @pytest.mark.it('Battle raises exception when attacking pokemon has already fainted')
    def test_battle__take_turn__with_fainted_pokemon_raises_exception(self):
        test_pokemon_1 = FirePokemon('Firestrong', 100, 40, 'Inferno')
        test_pokemon_2 = GrassPokemon('Weakgrass', 60, 10, 'Wilt')
        test_battle = Battle(test_pokemon_1, test_pokemon_2)

        test_battle.take_turn()

        with pytest.raises(Exception) as exc_info:
            test_battle.take_turn()

        assert str(exc_info.value) == "Weakgrass has fainted"