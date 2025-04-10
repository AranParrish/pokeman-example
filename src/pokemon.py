class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move
        self.__has_fainted = False

    def use_move(self):
        return f"{self.name} used {self.move}"

    def take_damage(self, damage):
        self.hit_points -= damage

        if self.hit_points <= 0:
            self.__has_fainted = True

    def has_fainted(self):
        return self.__has_fainted

    def get_multiplier(self, other_pokemon):
        if other_pokemon.pokemon_type == self.strong_against:
            return 1.5
        if other_pokemon.pokemon_type == self.weak_against:
            return 0.5
        return 1.0

    def __str__(self):
        return f"Pokemon: {self.name}, Type: {self.pokemon_type}"


class FirePokemon(Pokemon):
    pokemon_type = "fire"
    strong_against = "grass"
    weak_against = "water"


class GrassPokemon(Pokemon):
    pokemon_type = "grass"
    strong_against = "water"
    weak_against = "fire"


class WaterPokemon(Pokemon):
    pokemon_type = "water"
    strong_against = "fire"
    weak_against = "grass"


class NormalPokemon(Pokemon):
    pokemon_type = "normal"
    strong_against = None
    weak_against = None
