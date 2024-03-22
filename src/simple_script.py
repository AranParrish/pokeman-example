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
    "Move": "Fire blast",
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

# Trainer 1 capturing pokemon
trainer_1 = input('Please enter first trainer name --> ')
trainer_1 = Trainer(trainer_1)

print("Name", "Hit Points", "Move", "Attack damage", "Type", sep="\t")
for _, pokemon in pokemon_dict.items():
    print(pokemon["Name"], pokemon["Hit Points"], pokemon["Move"], 
          pokemon["Attack damage"], pokemon["Type"], sep="\t")

trainer_1_pokemon = input(f'Hello {trainer_1.name}, now enter name of pokemon to catch --> ')
selected_pokemon = pokemon_dict[trainer_1_pokemon.lower()]
class_selection_pokemon = type_dict[selected_pokemon["Type"]]

pokemon_1 = class_selection_pokemon(selected_pokemon["Name"],
                                     selected_pokemon["Hit Points"],
                                     selected_pokemon["Attack damage"],
                                     selected_pokemon["Move"])

trainer_1.throw_pokeball(pokemon_1)

print(f"{trainer_1.name} caught {pokemon_1.name}!")

# Trainer 2 capturing pokemon
trainer_2 = input('Please enter second trainer name --> ')
trainer_2 = Trainer(trainer_2)

print("Name", "Hit Points", "Move", "Attack damage", "Type", sep="\t")
for _, pokemon in pokemon_dict.items():
    print(pokemon["Name"], pokemon["Hit Points"], pokemon["Move"], 
          pokemon["Attack damage"], pokemon["Type"], sep="\t")

trainer_2_pokemon = input(f'Hello {trainer_2.name}, now enter name of pokemon to catch --> ')
selected_pokemon = pokemon_dict[trainer_2_pokemon.lower()]
class_selection_pokemon = type_dict[selected_pokemon["Type"]]

pokemon_2 = class_selection_pokemon(selected_pokemon["Name"],
                                     selected_pokemon["Hit Points"],
                                     selected_pokemon["Attack damage"],
                                     selected_pokemon["Move"])

trainer_2.throw_pokeball(pokemon_2)

print(f"{trainer_2.name} caught {pokemon_2.name}!")