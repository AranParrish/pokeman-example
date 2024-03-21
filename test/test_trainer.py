from src.trainer import Trainer
from src.pokemon import Pokemon
from src.pokeball import Pokeball
import pytest, types

@pytest.fixture
def pikachu():
    return ['Pikachu', 50, 20, 'Headbutt']

@pytest.mark.describe('Attribute Tests')
class TestAttributes:    
    @pytest.mark.it('Has a belt attribute')
    def test_trainer__has_belt_attribute(self):
        test_trainer = Trainer()
        assert isinstance(test_trainer.belt, list)
    
    @pytest.mark.it('Belt contains 6 pokeballs')
    def test_trainer__has_belt_with_6_pokeballs(self):
        test_trainer = Trainer()
        assert len(test_trainer.belt) == 6
        assert all([isinstance(item, Pokeball) for item in test_trainer.belt])

@pytest.mark.describe('Throw pokeball method tests')
class TestThrowPokeball:
    @pytest.mark.it('Can catch a pokemon in a pokeball')
    def test_trainer__can_catch_a_pokemon_in_a_pokeball(self, pikachu):
        test_trainer = Trainer()
        test_pokemon = Pokemon(*pikachu)
        test_trainer.throw_pokeball(test_pokemon)
        assert any([pokeball.current_pokemon is test_pokemon for pokeball in test_trainer.belt])

    @pytest.mark.it('Can catch up to 6 pokemon')
    def test_trainer__can_catch_6_pokemon(self, pikachu):
        test_trainer = Trainer()
        test_pokemon_1 = Pokemon(*pikachu)
        test_pokemon_2 = Pokemon(*pikachu)
        test_pokemon_3 = Pokemon(*pikachu)
        test_pokemon_4 = Pokemon(*pikachu)
        test_pokemon_5 = Pokemon(*pikachu)
        test_pokemon_6 = Pokemon(*pikachu)
        test_trainer.throw_pokeball(test_pokemon_1)
        test_trainer.throw_pokeball(test_pokemon_2)
        test_trainer.throw_pokeball(test_pokemon_3)
        test_trainer.throw_pokeball(test_pokemon_4)
        test_trainer.throw_pokeball(test_pokemon_5)
        test_trainer.throw_pokeball(test_pokemon_6)
        assert all([pokeball.current_pokemon is not None for pokeball in test_trainer.belt])
        
    @pytest.mark.it("Can't catch more than 6 pokemon")
    def test_trainer__cannot_catch_more_than_6_pokemon(self, pikachu):
        test_trainer = Trainer()
        test_pokemon_1 = Pokemon(*pikachu)
        test_pokemon_2 = Pokemon(*pikachu)
        test_pokemon_3 = Pokemon(*pikachu)
        test_pokemon_4 = Pokemon(*pikachu)
        test_pokemon_5 = Pokemon(*pikachu)
        test_pokemon_6 = Pokemon(*pikachu)
        test_pokemon_7 = Pokemon(*pikachu)
        test_trainer.throw_pokeball(test_pokemon_1)
        test_trainer.throw_pokeball(test_pokemon_2)
        test_trainer.throw_pokeball(test_pokemon_3)
        test_trainer.throw_pokeball(test_pokemon_4)
        test_trainer.throw_pokeball(test_pokemon_5)
        test_trainer.throw_pokeball(test_pokemon_6)     
        with pytest.raises(Exception) as exc_info:
            test_trainer.throw_pokeball(test_pokemon_7)
        assert "All pokeballs full" in str(exc_info.value)
        