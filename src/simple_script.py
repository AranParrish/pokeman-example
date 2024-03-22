from src.trainer import Trainer
from src.pokeball import Pokeball
from src.pokemon import Pokemon, NormalPokemon, GrassPokemon, FirePokemon, WaterPokemon
from src.battle import Battle
from src.pokemon_data import pokemon_dict


type_dict = {
    "normal": NormalPokemon,
    "grass": GrassPokemon,
    "fire": FirePokemon,
    "water": WaterPokemon
}


def select_pokemon(trainer):
    print("\nName       Hit Points  Move         Damage      Type")
    for _, pokemon in pokemon_dict.items():
        print(f'{pokemon["Name"]:<10} {pokemon["Hit Points"]:<11} {pokemon["Move"]:<13}' 
            f'{pokemon["Attack damage"]:<11} {pokemon["Type"].capitalize():<6}')

    selected_pokemon = input(f'\nHello {trainer.name}, now enter name of pokemon to catch --> ')
    while True:
            try:    
                selected_pokemon = pokemon_dict[selected_pokemon.lower()]
            except KeyError:
                print(f'Sorry, unrecognised Pokemon. Please try again.')
                selected_pokemon = input(f'Enter name of pokemon to catch --> ')
            else:
                break

    class_selection_pokemon = type_dict[selected_pokemon["Type"]]

    pokemon = class_selection_pokemon(selected_pokemon["Name"],
                                        selected_pokemon["Hit Points"],
                                        selected_pokemon["Attack damage"],
                                        selected_pokemon["Move"])

    trainer.throw_pokeball(pokemon)

    print(f"{trainer.name} caught {pokemon.name}!")


# Trainer 1 capturing pokemon
trainer_1 = input('\nPlease enter first trainer name --> ')
trainer_1 = Trainer(trainer_1)
select_pokemon(trainer_1)

# Trainer 2 capturing pokemon
trainer_2 = input('\nPlease enter second trainer name --> ')
trainer_2 = Trainer(trainer_2)

select_pokemon(trainer_2)

print('\n\nLET BATTLE COMMENCE!\n')

battle = Battle(trainer_1.belt[0].current_pokemon, trainer_2.belt[0].current_pokemon)

print(battle,'\n')

current_trainer, next_trainer = trainer_1, trainer_2

while (winner := battle.get_winner()) is None:
    print(battle.take_turn(0.3))
    current_trainer, next_trainer = next_trainer, current_trainer

print(f'\n{next_trainer.name}\'s pokemon {winner} wins!')