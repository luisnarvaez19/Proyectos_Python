from edu.G_Python.warrior.DefensiveWarrior import DefensiveWarrior
from edu.G_Python.warrior.OffensiveWarrior import OffensiveWarrior


class SuperWarrior(OffensiveWarrior, DefensiveWarrior):
    def __init__(self, id, warrior_type, weapon_type, health_points, attack_rating, defense_rating, special_defense, special_attack, ):
        if self.validate_values("Special defense", special_defense, 11, 20):
            self.__special_defense = special_defense
        if self.validate_values("Special attack", special_attack, 11, 20):
            self.__special_attack = special_attack

        super().__init__(self, id, warrior_type, weapon_type, health_points, attack_rating, defense_rating)
