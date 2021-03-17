
from com.G_Python.warrior.SuperWarrior import SuperWarrior
from com.G_Python.warrior.Coach import Coach
from com.G_Python.warrior.Warrior import Warrior

"""
prohibited without the written consent of the copyright owner.
"""
import csv
# Source packages.

def read_warriors(file_warriors):
    list_warriors = []
    with open(file_warriors) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

    # row[0]   1,BOXER,punch,79,6,9,14,17
    for row in csv_reader:
        warrior = SuperWarrior(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        list_warriors.append(warrior)

    return list_warriors

# Selecciona un guerrero vivo
def select_warriors(coach):
    count = 0
    print('Tu lista de guerreros es:')
    for i in coach.get_lista_guerreros():
        if i.is_alive():
            print(str(i))
            count += 1
    if count == 0:
        return None
    else:
        id = int(input('Selecciona el id del guerrero con el que quieres pelear: '))
        fighter = coach.find_by_id(id)
        return fighter


def main():
    """Function main of the module.

The function main of this module is used to perform the Game.

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
#>>> main()
"""


print("Welcome to the Game.")
print("Let's start to set the configuration of each game user. \n")

# Get configuration for Game User 1.
print("For Game User 1: \n")
coach1_name=input('Introduzca el nombre del jugador 1: ')
print("For Game User 2: \n")
coach2_name=input('Introduzca el nombre del jugador 2: ')
# Get configuration for Game User 2.
print("------------------------------------------------------------------")
print("The Game starts...")
print("------------------------------------------------------------------")

# Get a copy of the list of warriors for both coaches
list_warriors_1=read_warriors("coach_1_warriors.csv")
coach1 = Coach(coach1_name, list_warriors_1)


list_warriors_2=read_warriors("coach_2_warriors.csv")
coach2 = Coach(coach2_name, list_warriors_2)

# Choose first warriors for both coaches

# Create the algorithm of the game. The coaches will fight until all their warriors are defeated.
# If a warrior is defeated, the coach should select the next warrior to enter the combat.
sel1 = False
sel2 = False
while (coach1.is_undefeated() or coach2.is_undefeated()):
    if not sel1:
        fighter1 = select_warriors(coach1)
        if fighter1 is None:
            print('The player 2' + coach2_name+' win')

    if not sel2:
        fighter2 = select_warriors(coach2)
        if fighter2 is None:
        print('The player 1' + coach1_name+' win')


    while fighter1.is_alive() and fighter2.is_alive():
        fighter1.fight_attack(fighter2)
        fighter2.fight_attack(fighter1)

    sel1 = not fighter1.is_alive()
    sel2 = not fighter2.is_alive()

print("------------------------------------------------------------------")
print("The Game has end...")
print("------------------------------------------------------------------")
# SHOW THE WINNER/DRAW


print("------------------------------------------------------------------")
print("Statistics")
print("------------------------------------------------------------------")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF