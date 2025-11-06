import random
from random import randint
import game
from core import *


class Goblin:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = 1
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"gobli {self.name} is angry")

    def attack(self,player):
        roll = game.roll_dice(6)
        if self.weapon == "knife":
            roll *= 0.5
        elif self.weapon == "sword":
            roll *= 1
        else:
            roll *= 1.5
        roll += player.power
        player.hp -= roll
        return player

    def run_away(self):
        pass