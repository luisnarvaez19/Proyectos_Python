from com.G_Python.warrior.WarriorType import WarriorType
from com.G_Python.warrior.WeaponType import WeaponType
from com.G_Python.warrior.Warrior import Warrior


class Coach:

    def __init__(self, coach_name, lista_guerreros):

        if not isinstance(coach_name, str):
            raise ValueError("Coach name must be a str")
        else:
            self.__coach_name = coach_name

        if not isinstance(lista_guerreros, list):
            raise ValueError("Lista guerreros must be a list")
        else:
            if (len(lista_guerreros) == 0):
                raise ValueError("Lista guerreros must not be empty")
            else:
                self.__lista_guerreros = lista_guerreros

    def get_coach_name(self):
        return self.__coach_name

    def get_lista_guerreros(self):
        return self.__lista_guerreros

    # agregar setters.

    def is_undefeated(self):

        for i in self.__lista_guerreros:
            if i.get_health_points() > 0:
                return True
        return False

    def surrender(self):
        for i in self.__lista_guerreros:
            i.set_health_points(0)
        return "Has abandonado la partida."

    def __str__(self):
        resultado = ""
        for i in self.__lista_guerreros:
            resultado += str(i.get_warrior_type().name) + ' with a ' + str(
                i.get_weapon_type().name) + ' and health: ' + str(i.get_health_points()) + "\n"
        return resultado

    def __repr__(self):
        for i in self.__lista_guerreros:
            return id + "\t" + i.get_warrior_type().name + "\t" + i.get_weapon_type().name


    def find_by_id(self, id):
        for i in self.__lista_guerreros:
            if i.id == id:
                return i
        return None


def main():
    """Function main of the module.

    The function main of this module is used to test the Class Coach.

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
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Coach with an empty list.")
    print("=================================================================.")
    coach1_warriors = []

    try:
        coach1 = Coach("", coach1_warriors)
        print(
            "Test FAIL. It should raise a ValueError exception. Check the method __init__() based on the object: " + str(
                coach1))
    except ValueError as value_error:
        print("Test PASS. The exception was raised: " + str(value_error) + " .")

    print("=================================================================.")
    print("Test Case 2: Create a Coach with a NON empty list.")
    print("=================================================================.")
    warrior1 = Warrior(1, WarriorType.BOXER, WeaponType.KICK, 99, 10, 7)
    warrior2 = Warrior(2, WarriorType.BOXER, WeaponType.KICK, 99, 9, 8)
    coach2_warriors = []
    coach2_warriors.append(warrior1)
    coach2_warriors.append(warrior2)
    try:
        coach2 = Coach("Rocky Balboa", coach2_warriors)
        print("The following coach has been generated: " + str(coach2))
        print("Test PASS. The method __init__() has been implemented correctly.")
    except ValueError as value_error:
        print("Test FAIL. Check the method __init__(): " + str(value_error))

    print("=================================================================.")
    print("Test Case 3: Human-readable format of the object.")
    print("=================================================================.")
    coach3_warriors = []
    coach3_warriors.append(warrior1)
    coach3_warriors.append(warrior2)
    coach3 = Coach("Rocky Balboa", coach3_warriors)
    print(str(coach3))
    if str(coach3) == "Rocky Balboa with 2 warriors.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__().")

    print("=================================================================.")
    print("Test Case 4: Coach undefeated?¿?.")
    print("=================================================================.")
    coach4_warriors = []
    coach4_warriors.append(warrior1)
    coach4_warriors.append(warrior2)
    coach4 = Coach("Rocky Balboa", coach3_warriors)

    if coach4.is_undefeated():
        print("Test PASS. The method is_undefeated() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method is_undefeated().")

    coach4.surrender()

    if coach4.is_undefeated():
        print("Test FAIL. Check the method is_undefeated().")
    else:
        print("Test PASS. The method is_undefeated() has been implemented correctly.")


# Checking whether this script is executed just itself alone.
if __name__ == "__main__":
    main()

# EOF
