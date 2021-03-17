import enum

import self as self

from edu.G_Python.warrior.WarriorType import WarriorType
from edu.G_Python.warrior.WeaponType import WeaponType


class Warrior:

    def __init__(self, id, warrior_type, weapon_type, health_points, attack_rating, defense_rating):
        if not isinstance(id, int):
            raise ValueError("WarriorType must be an integer")
        else:
            self.__id = id
        if not isinstance(warrior_type, enum.Enum):
            raise TypeError("WarriorType must be an enumerate")
        else:
            self.__warrior_type = warrior_type
        if not isinstance(weapon_type, WeaponType):
            raise TypeError("WeaponType must be an enumerate")
        else:
            self.__weapon_type = weapon_type
        if self.validate_values("Health", health_points, 1, 100):
            self.__health_points = health_points
        if self.validate_values("Attach_rating", attack_rating, 1, 10):
            self.__attack_rating = attack_rating
        if self.validate_values("Defense_rating", defense_rating, 1, 10):
            self.__defense_rating = defense_rating

    def get_warrior_type(self):
        return self.__warrior_type

    def get_weapon_type(self):
        return self.__weapon_type

    def get_health_points(self):
        return self.__health_points

    def get_attack_rating(self):
        return self.__attack_rating

    def get_defense_raiting(self):
        return self.__defense_rating

    def set_weapon_type(self, weapon_type):
        if not isinstance(weapon_type, enumerate):
            raise TypeError("Weapon_type must be an enumerate")
        else:
            self.__weapon_type = weapon_type

    def set_health_points(self, health_points):
        if self.validate_values("Health", health_points, 1, 100):
            self.__health_points = health_points

    def set_attack_rating(self, attack_rating):
        if self.validate_values("Attach_rating", attack_rating, 1, 10):
            self.__attack_rating = attack_rating

    def set_defense_rating(self, defense_rating):
        if self.validate_values("Defense_rating", defense_rating, 1, 10):
            self.__defense_rating = defense_rating

    def validate_values(self, name, value, minimum, maximum):
        if not isinstance(value, int):
            raise TypeError(name + " must be an int")
        else:
            if minimum > value > maximum:
                raise TypeError(name + " must be between: " + minimum + " and " + maximum)
        return True

    def is_alive(self):
        # alive if health > 0
        if self.__health_points > 0:
            return True

    def fight_defense(self, points_of_damage):
        if not isinstance(points_of_damage, int):
            raise TypeError("Points_of_damage must be an int")
        else:
            if self.__defense_rating > points_of_damage:
                return False
            else:
                self.__health_points += self.__defense_rating - points_of_damage
                return True

    def fight_attack(self, warrior_to_attack):
        if not isinstance(warrior_to_attack, Warrior):
            raise TypeError("Warrior_to_attach must be an Warrior")
        else:
            warrior_to_attack.fight_defense(self.__attack_rating)

    def __str__(self):
        return str(self.__id) + ' ' + self.__warrior_type.name + ' ' + self.__weapon_type.name + ' ' + str(
            self.__health_points) + ' ' + str(self.__attack_rating) + ' ' + str(self.__defense_rating)


def main():
    """Function main of the module.

    The function main of this module is used to test the Class Warrior.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
    """

    print("=================================================================.")
    print("Test Case 1: Create a Warrior.")
    print("=================================================================.")
    warrior1 = Warrior(1, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 8, 9)

    if warrior1.get_warrior_type().name == 'GLADIATOR':
        print("Test PASS. The parameter warrior_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_weapon_type().name == "SWORD":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_defense_raiting() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    warrior2 = Warrior(2, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10)

    '''
    if str(warrior2) == "GLADIATOR with a SWORD":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__().")
    '''

    print("=================================================================.")
    print("Test Case 3: Warrior alive?¿?.")
    print("=================================================================.")
    warrior3 = Warrior(3, WarriorType.UFC, WeaponType.KICK, 97, 8, 9)

    if warrior3.is_alive():
        warrior3.fight_defense(200)  # With this the warrior should be retired.

        if not warrior3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")

    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    warrior4 = Warrior(4, WarriorType.MMA, WeaponType.ELBOW, 93, 9, 6)

    warrior4.fight_defense(70)

    if warrior4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")

    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    warrior5 = Warrior(5, WarriorType.BOXER, WeaponType.PUNCH, 99, 10, 7)
    warrior6 = Warrior(6, WarriorType.BOXER, WeaponType.PUNCH, 99, 9, 8)

    warrior_hit = warrior5.fight_attack(warrior6)

    if warrior_hit:
        if warrior6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack(). 97")
    else:
        if warrior6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack(). 99")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()

# EOF
