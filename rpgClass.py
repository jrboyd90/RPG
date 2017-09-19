
#Making a Hero class
class Hero:
    def __init__(self,health='10',power='5'):
        self.health = health
        self.power = power
    def attack(enemy):
        enemy.health -= self.power
            print("You do {} damage to the goblin.".format(self.power))
            if enemy.health <= 0:
                print("The goblin is dead.")
    def alive():
        if self.health > 0:
            return True
        else:
            return False
    def print_status():
        print("You have {} health and {} power.".format(self.health, self.power))

# Making a Goblin class
class Goblin:
    def __init__(self,health='6',power='2'):
        self.health = health
        self.power = power
    def attack(enemy):
        enemy.health -= self.power
            print("The goblin does {} damage to you.".format(self.power))
            if enemy.health <= 0:
                print("You are dead.")
    def alive():
        if self.health > 0:
            return True
        else:
            return False
    def print_status():
        print("The Goblin has {} health and {} power.".format(self.health, self.power))
