#Make a Character class
class Character:
    def __init__(self,health,power):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
#Making a Hero class
class Hero (Character):
    def attack(self,enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

# Making a Goblin class
class Goblin (Character):
    def attack(self,enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")
    def print_status(self):
        print("The Goblin has {} health and {} power.".format(self.health, self.power))
