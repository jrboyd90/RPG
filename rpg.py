from rpgClass import Hero
from rpgClass import Goblin


def main():
    link = Hero()
    goblin = Goblin()

    while goblin.alive() and link.alive():
        print("You have {} health and {} power.".format(link.health, link.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            link.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            goblin.attack(link)

main()
