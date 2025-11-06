import random
from random import randint
import game


class Orc:
    def __init__(self,name):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed = randint(0, 5)
        self.power = randint(10, 15)
        self.armor_rating = randint(2, 8)
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"Orc {self.name} shouts")

    def attack(self, player):
        roll = game.roll_dice(6)
        if self.weapon == "knife":
            roll *= 0.5
        elif self.weapon == "sword":
            roll *= 1
        else:
            roll *= 1.5
        roll += player.power
        player.hp -= roll