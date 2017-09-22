import random
import time


#Make a Character class
class Character:
    def __init__(self):
        self.name = '<undefined>'
        self.health = 5
        self.power = 5
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, enemy):
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        time.sleep(1.5)
        if self.health <= 0:
            print("{} is dead.".format(self.name))
    def print_status(self):
        print("\n{} has {} health and {} power.".format(self.name,self.health, self.power))

#Make a Hero class
class Hero (Character):
    def __init__(self):
        super().__init__()
        self.name = 'hero'
        self.health = 10
        self.power = 5
    def attack(self,enemy):
        if random.randint(1,5) != 1:
            super().attack(enemy)
        else:
            print("DOUBLE ATTACK! {} attacks {}".format(self.name, enemy.name))
            enemy.receive_damage(self.power * 2)


# Make a Goblin class
class Goblin (Character):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin'
        self.health = 50
        self.power = 2

#Make a medic class
class Medic (Character):
    def __init__(self):
        super().__init__()
        self.name = 'Medic'
        self.health = 7
        self.power = 2
    def receive_damage(self,points):
        super().receive_damage(points)
        if random.randint(1,2) == 1 and self.health > 0:
            self.health += 2
            print('{} heals 2 health points'.format(self.name))
# Make a shadow class
class Shadow (Character):
    def __init__(self):
        super().__init__()
        self.name = 'Shadow'
        self.health = 1
        self.power = 4
    def receive_damage(self,points):
        if random.randint(1,10) == 1:
            super().receive_damage(points)
        else:
            print('{} dodges attack'.format(self.name))
# Make a zombie Character
class Zombie (Character):
    def __init__(self):
        super().__init__()
        self.name = 'Zombie'
        self.health = 1
        self.power = 1
    def alive(self):
        if self.health > 0:
            return True
        else:
            return True
class Mage (Character):
    def __init__(self):
        super().__init__()
