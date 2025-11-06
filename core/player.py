import random
from random import randint

import game



class Player:
    def __init__(self,name,):
        self.name = name
        self.hp = 50
        self.speed = randint(5,10)
        self.power = randint(5,10)
        self.armor_rating = randint(5,15)
        self.profession = random.choice(["fighter","cure"])

    def speak(self):
        print(f"Hllow i m {self.profession} ")

    def attack(self,monster):
        roll = game.roll_dice(6)
        if self.profession == "fighter":
            roll += 2
        roll += monster.power
        monster.hp -= roll

