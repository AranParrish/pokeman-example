from src.trainer import Trainer
from src.pokeball import Pokeball
from src.pokemon import Pokemon, NormalPokemon, GrassPokemon, FirePokemon, WaterPokemon
from src.battle import Battle

flareon = {
    "Name": "Flareon",
    "Hit Points": 65,
    "Move": "Fire blast",
    "Attack damage": 20,
    "Type": "fire"
}

leafeon = {
    "Name": "Leafeon",
    "Hit Points": 65,
    "Move": "Giga drain",
    "Attack damage": 17,
    "Type": "grass"
}

type_dict = {
    "normal": NormalPokemon,
    "grass": GrassPokemon,
    "fire": FirePokemon,
    "water": WaterPokemon
}

pokemon_dict = {
    "flareon": flareon,
    "leafeon": leafeon
    }



def select_pokemon(trainer):
    print("Name       Hit Points  Move         Damage      Type")
    for _, pokemon in pokemon_dict.items():
        print(f'{pokemon["Name"]:<10} {pokemon["Hit Points"]:<11} {pokemon["Move"]:<13}' 
            f'{pokemon["Attack damage"]:<11} {pokemon["Type"].capitalize():<6}')

    selected_pokemon = input(f'Hello {trainer.name}, now enter name of pokemon to catch --> ')
    selected_pokemon = pokemon_dict[selected_pokemon.lower()]
    class_selection_pokemon = type_dict[selected_pokemon["Type"]]

    pokemon = class_selection_pokemon(selected_pokemon["Name"],
                                        selected_pokemon["Hit Points"],
                                        selected_pokemon["Attack damage"],
                                        selected_pokemon["Move"])

    trainer.throw_pokeball(pokemon)

    print(f"{trainer.name} caught {pokemon.name}!")


# Trainer 1 capturing pokemon
trainer_1 = input('Please enter first trainer name --> ')
trainer_1 = Trainer(trainer_1)
select_pokemon(trainer_1)

# Trainer 2 capturing pokemon
trainer_2 = input('Please enter second trainer name --> ')
trainer_2 = Trainer(trainer_2)

select_pokemon(trainer_2)

print('Let battle commence!')

battle = Battle(trainer_1.belt[0].current_pokemon, trainer_2.belt[0].current_pokemon)

print(battle)