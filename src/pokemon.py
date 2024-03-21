class Pokemon():
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