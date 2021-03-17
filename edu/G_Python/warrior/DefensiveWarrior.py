import random

import self

from com.G_Python.warrior.Warrior import Warrior


class DefensiveWarrior(Warrior):
    def __init__(self, id, warrior_type, weapon_type, health_points, attack_rating, defense_rating, defense_special):
        if self.validate_values("Defense special", defense_special, 11, 20):
            self.__defense_special = defense_special
        super().__init__(self, id, warrior_type, weapon_type, health_points, attack_rating, defense_rating)

    def get_defense_special(self):
        return self.__defense_rating

    def set_defense_special(self, defense_special):
        if self.validate_values("Defense_special", defense_special, 11, 20):
            self.__defense_special = defense_special

    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("Points_of_damage must be an int")
        else:
            if random.random() > 0.5:
                if self.__defense_rating > points_of_damage:
                    return False
                else:
                    self.__health_points += self.__defense_rating - points_of_damage
                    return True
            else:
                if self.__defense_special > points_of_damage:
                    return False
                else:
                    self.__health_points += self.__defense_special - points_of_damage
                    return True
