from rpg2Class import *

hero = Hero()
goblin = Goblin()
talon = Medic()
maytrix = Shadow()
zombie = Zombie()

def battle(hero,enemy):


    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
            continue
        if enemy.alive():
            enemy.attack(hero)
            time.sleep(1.5)

battle(zombie,goblin)
