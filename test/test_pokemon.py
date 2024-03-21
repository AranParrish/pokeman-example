from src.pokemon import Pokemon
import pytest

@pytest.fixture
def pikachu():
    return ['Pikachu', 50, 20, 'Headbutt']


def test_pokemon_constructor_initialises_with_given_attributes(pikachu):
    test_pokemon = Pokemon(*pikachu)

    assert test_pokemon.name == 'Pikachu'
    assert test_pokemon.hit_points == 50
    assert test_pokemon.attack_damage == 20
    assert test_pokemon.move == 'Headbutt'


def test_pokemon_has__use_move__method(pikachu):
    test_pokemon = Pokemon(*pikachu)
    expected = 'Pikachu used Headbutt'

    result = test_pokemon.use_move()

    assert result == expected


def test_pokemon_has__take_damage_method(pikachu):
    test_pokemon = Pokemon(*pikachu)
    expected = 20

    test_pokemon.take_damage(30)

    assert test_pokemon.hit_points == expected


def test_pokemon_has__has_fainted__method(pikachu):
    test_pokemon = Pokemon(*pikachu)

    assert isinstance(test_pokemon.has_fainted(), bool)


def test_pokemon__has_fainted__switches_to_true_when_hit_points_0(pikachu):
    test_pokemon = Pokemon(*pikachu)

    test_pokemon.take_damage(50)

    assert test_pokemon.has_fainted()