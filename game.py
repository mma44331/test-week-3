import random
from core import orc,goblin,player


def start():
    player = create_player()
    monster = choose_random_monster()
    start = show_menu()
    print(start)
    if start == "Y":
        displaying_values(player, monster)
        battle(player,monster)

def displaying_values(player,monster):
    print(f"Player details :\n Player name:{player.name} \n Number of lives:{player.hp} \n The speed is: {player.speed} \n The power is: {player.power} \n Armor power: {player.armor_rating} \n Player type: {player.profession}")
    print(f"Monser details :\n Monser name:{monster.name} \n Number of lives:{monster.hp} \n The type monster is: {monster.type} \n The speed is: {monster.speed} \n The power is: {monster.power} \n Armor power: {monster.armor_rating} \n weapon type: {monster.weapon}")

def show_menu():
    print("Do you want to play?")
    while True:
        sta = input("enter 'Y' or 'N' ")
        sta = sta.upper()
        if "N" or "Y" in sta:
            break
    return sta

def create_player() -> player.Player:
    play = player.Player("moshe")
    return play


def choose_random_monster():
    temp = random.choice(['orc','goblin'])
    if temp == "orc":
        monster = orc.Orc("Doby")
    else:
        monster = goblin.Goblin("Momy")
    return monster

def chack_attack(validity, attacked) ->bool:
    roll_validity = roll_dice(20)
    roll_validity += validity.speed
    if roll_validity > attacked.armor_rating:
        return True
    return False

def test_live(attacked):
    if attacked.hp <= 0:
        return True
    return False



# def player_attack(player, monster):
#     roll = roll_dice(6)
#     if player.profession == "fighter":
#         roll += 2
#     roll += monster.power
#     monster.hp -= roll
#     if test_live(monster):
#         return False

def battle(player: player.Player, monster):
    roll_player = roll_dice(6)
    roll_player += player.speed
    roll_monster = roll_dice(6)
    roll_monster += monster.speed

    if roll_monster > roll_player:
        flage = chack_attack(monster,player)
        if flage:
            if monster.type == "goblin":
                game = goblin.Goblin.attack(player)
            else:
                game = orc.Orc.attack(player)

    else:
        flage = chack_attack(monster,player)
        if flage:
            game = player.attack(monster)




def roll_dice(sides):
    roll = random.randint(1,sides)
    return roll