from rpgClass import *


def main():
    link = Hero(10,6)
    goblin = Goblin(6,2)

    while goblin.alive() and link.alive():
        link.print_status()
        goblin.print_status()
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

        if goblin.alive() > 0:
            goblin.attack(link)

main()
