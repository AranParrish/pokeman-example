from src.pokemon import Pokemon, FirePokemon, GrassPokemon, WaterPokemon, NormalPokemon
import pytest


@pytest.fixture
def pikachu():
    return ["Pikachu", 50, 20, "Headbutt"]


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


@pytest.mark.describe("Tests for Pokemon parent class")
class TestPokemonParent:
    @pytest.mark.it("Initialises with given attributes")
    def test_pokemon_constructor_initialises_with_given_attributes(self, pikachu):
        test_pokemon = Pokemon(*pikachu)

        assert test_pokemon.name == "Pikachu"
        assert test_pokemon.hit_points == 50
        assert test_pokemon.attack_damage == 20
        assert test_pokemon.move == "Headbutt"

    @pytest.mark.it("Has use move method")
    def test_pokemon_has__use_move__method(self, pikachu):
        test_pokemon = Pokemon(*pikachu)
        expected = "Pikachu used Headbutt"

        result = test_pokemon.use_move()

        assert result == expected

    @pytest.mark.it("Has take damage method")
    def test_pokemon_has__take_damage_method(self, pikachu):
        test_pokemon = Pokemon(*pikachu)
        expected = 20

        test_pokemon.take_damage(30)

        assert test_pokemon.hit_points == expected

    @pytest.mark.it("Has fainted method")
    def test_pokemon_has__has_fainted__method(self, pikachu):
        test_pokemon = Pokemon(*pikachu)

        assert isinstance(test_pokemon.has_fainted(), bool)

    @pytest.mark.it("Has fainted is true when 0 hit points")
    def test_pokemon__has_fainted__switches_to_true_when_hit_points_0(self, pikachu):
        test_pokemon = Pokemon(*pikachu)

        test_pokemon.take_damage(50)

        assert test_pokemon.has_fainted()

    @pytest.mark.it("Returns name and type of pokemon")
    def test_pokemon__returns_name_and_type(self, pikachu, flareon, vaporeon, leafeon):
        test_pokemon_1 = NormalPokemon(*pikachu)
        test_pokemon_2 = FirePokemon(*flareon)
        test_pokemon_3 = GrassPokemon(*leafeon)
        test_pokemon_4 = WaterPokemon(*vaporeon)
        assert str(test_pokemon_1) == "Pokemon: Pikachu, Type: normal"
        assert str(test_pokemon_2) == "Pokemon: Flareon, Type: fire"
        assert str(test_pokemon_3) == "Pokemon: Leafeon, Type: grass"
        assert str(test_pokemon_4) == "Pokemon: Vaporeon, Type: water"


@pytest.mark.describe("Tests for fire pokemon class")
class TestFirePokemon:
    def test_pokemon__fire_type_inherits_from_pokeman(self, flareon):
        test_fire_pokemon = FirePokemon(*flareon)
        assert isinstance(test_fire_pokemon, Pokemon)

    def test_pokemon__fire_pokemon_initialises_with_class_attributes(self, flareon):
        test_fire_pokemon = FirePokemon(*flareon)
        assert test_fire_pokemon.pokemon_type == "fire"
        assert test_fire_pokemon.strong_against == "grass"
        assert test_fire_pokemon.weak_against == "water"

    def test_pokemon__fire_pokemon_has_get_multipler_method(self, flareon):
        test_fire_pokemon = FirePokemon(*flareon)
        assert isinstance(test_fire_pokemon.get_multiplier(test_fire_pokemon), float)

    def test_pokemon__fire_pokemon_get_multiplier_is_1_against_fire(self, flareon):
        test_fire_pokemon_1 = FirePokemon(*flareon)
        test_fire_pokemon_2 = FirePokemon("Flareon_2", 50, 20, "Headbutt")
        assert test_fire_pokemon_1.get_multiplier(test_fire_pokemon_2) == 1

    def test_pokemon__fire_pokemon_get_multiplier_is_higher_against_grass(
        self, flareon, leafeon
    ):
        test_fire_pokemon = FirePokemon(*flareon)
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert test_fire_pokemon.get_multiplier(test_grass_pokemon) == 1.5

    def test_pokemon__fire_pokemon_get_multiplier_is_lower_against_water(
        self, flareon, vaporeon
    ):
        test_fire_pokemon = FirePokemon(*flareon)
        test_water_pokemon = WaterPokemon(*vaporeon)
        assert test_fire_pokemon.get_multiplier(test_water_pokemon) == 0.5

    def test_pokemon__fire_pokemon_get_multiplier_is_1_against_normal(
        self, flareon, eevee
    ):
        test_fire_pokemon = FirePokemon(*flareon)
        test_normal_pokemon = NormalPokemon(*eevee)
        assert test_fire_pokemon.get_multiplier(test_normal_pokemon) == 1


@pytest.mark.describe("Tests for grass pokemon class")
class TestGrassPokemon:
    def test_pokemon__grass_type_inherits_from_pokeman(self, leafeon):
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert isinstance(test_grass_pokemon, Pokemon)

    def test_pokemon__grass_pokemon_initialises_with_class_attributes(self, leafeon):
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert test_grass_pokemon.pokemon_type == "grass"
        assert test_grass_pokemon.strong_against == "water"
        assert test_grass_pokemon.weak_against == "fire"

    def test_pokemon__grass_pokemon_has_get_multipler_method(self, leafeon):
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert isinstance(test_grass_pokemon.get_multiplier(test_grass_pokemon), float)

    def test_pokemon__grass_pokemon_get_multiplier_is_1_against_grass(self, leafeon):
        test_grass_pokemon_1 = GrassPokemon(*leafeon)
        test_grass_pokemon_2 = GrassPokemon("Leafon_2", 50, 20, "Headbutt")
        assert test_grass_pokemon_1.get_multiplier(test_grass_pokemon_2) == 1

    def test_pokemon__grass_pokemon_get_multiplier_is_higher_against_water(
        self, leafeon, vaporeon
    ):
        test_grass_pokemon = GrassPokemon(*leafeon)
        test_water_pokemon = WaterPokemon(*vaporeon)
        assert test_grass_pokemon.get_multiplier(test_water_pokemon) == 1.5

    def test_pokemon__grass_pokemon_get_multiplier_is_lower_against_fire(
        self, flareon, leafeon
    ):
        test_fire_pokemon = FirePokemon(*flareon)
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert test_grass_pokemon.get_multiplier(test_fire_pokemon) == 0.5

    def test_pokemon__grass_pokemon_get_multiplier_is_1_against_normal(
        self, leafeon, eevee
    ):
        test_grass_pokemon = GrassPokemon(*leafeon)
        test_normal_pokemon = NormalPokemon(*eevee)
        assert test_grass_pokemon.get_multiplier(test_normal_pokemon) == 1


@pytest.mark.describe("Tests for water pokemon class")
class TestWaterPokemon:
    def test_pokemon__water_type_inherits_from_pokemon(self, vaporeon):
        test_water_pokemon = WaterPokemon(*vaporeon)
        assert isinstance(test_water_pokemon, Pokemon)

    def test_pokemon__water_pokemon_initialises_with_class_attributes(self, vaporeon):
        test_water_pokemon = WaterPokemon(*vaporeon)
        assert test_water_pokemon.pokemon_type == "water"
        assert test_water_pokemon.strong_against == "fire"
        assert test_water_pokemon.weak_against == "grass"

    def test_pokemon__water_pokemon_has_get_multipler_method(self, vaporeon):
        test_water_pokemon = WaterPokemon(*vaporeon)
        assert isinstance(test_water_pokemon.get_multiplier(test_water_pokemon), float)

    def test_pokemon__water_pokemon_get_multiplier_is_1_against_water(self, vaporeon):
        test_water_pokemon_1 = WaterPokemon(*vaporeon)
        test_water_pokemon_2 = WaterPokemon("Vaporeon", 50, 20, "Headbutt")
        assert test_water_pokemon_1.get_multiplier(test_water_pokemon_2) == 1

    def test_pokemon__water_pokemon_get_multiplier_is_higher_against_fire(
        self, vaporeon, flareon
    ):
        test_water_pokemon = WaterPokemon(*vaporeon)
        test_fire_pokemon = FirePokemon(*flareon)
        assert test_water_pokemon.get_multiplier(test_fire_pokemon) == 1.5

    def test_pokemon__water_pokemon_get_multiplier_is_lower_against_grass(
        self, vaporeon, leafeon
    ):
        test_water_pokemon = WaterPokemon(*vaporeon)
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert test_water_pokemon.get_multiplier(test_grass_pokemon) == 0.5

    def test_pokemon__water_pokemon_get_multiplier_is_1_against_normal(
        self, vaporeon, eevee
    ):
        test_water_pokemon = WaterPokemon(*vaporeon)
        test_normal_pokemon = NormalPokemon(*eevee)
        assert test_water_pokemon.get_multiplier(test_normal_pokemon) == 1


@pytest.mark.describe("Tests for normal pokemon class")
class TestNormalPokemon:
    def test_pokemon__normal_type_inherits_from_pokemon(self, eevee):
        test_normal_pokemon = NormalPokemon(*eevee)
        assert isinstance(test_normal_pokemon, Pokemon)

    def test_pokemon__normal_pokemon_initialises_with_class_attributes(self, eevee):
        test_normal_pokemon = NormalPokemon(*eevee)
        assert test_normal_pokemon.pokemon_type == "normal"
        assert test_normal_pokemon.strong_against == None
        assert test_normal_pokemon.weak_against == None

    def test_pokemon__normal_pokemon_has_get_multipler_method(self, eevee):
        test_normal_pokemon = NormalPokemon(*eevee)
        assert isinstance(
            test_normal_pokemon.get_multiplier(test_normal_pokemon), float
        )

    def test_pokemon__normal_pokemon_get_multiplier_is_1_against_normal(self, eevee):
        test_normal_pokemon_1 = NormalPokemon(*eevee)
        test_normal_pokemon_2 = NormalPokemon("Eevee", 50, 20, "Headbutt")
        assert test_normal_pokemon_1.get_multiplier(test_normal_pokemon_2) == 1

    def test_pokemon__normal_pokemon_get_multiplier_is_1_against_fire(
        self, eevee, flareon
    ):
        test_normal_pokemon = NormalPokemon(*eevee)
        test_fire_pokemon = FirePokemon(*flareon)
        assert test_normal_pokemon.get_multiplier(test_fire_pokemon) == 1

    def test_pokemon__normal_pokemon_get_multiplier_is_1_against_water(
        self, eevee, vaporeon
    ):
        test_normal_pokemon = NormalPokemon(*eevee)
        test_water_pokemon = WaterPokemon(*vaporeon)
        assert test_normal_pokemon.get_multiplier(test_water_pokemon) == 1

    def test_pokemon__normal_pokemon_get_multiplier_is_1_against_grass(
        self, eevee, leafeon
    ):
        test_normal_pokemon = NormalPokemon(*eevee)
        test_grass_pokemon = GrassPokemon(*leafeon)
        assert test_normal_pokemon.get_multiplier(test_grass_pokemon) == 1
