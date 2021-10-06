from _future_ import print_function

import random


# let
# 0 - stone
# 1 - paper
# 2 - scissor


def name_to_number(name):
    if name == "stone":
        name = 0
    elif name == "paper":
        name = 1
    elif name == "scissors":
        name = 2
    return name


def number_to_name(number):
    if number == 0:
        return "stone"
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissors"


def game(player_choice):
    print()
    name = player_choice
    print(name)
    number = name_to_number(name)
    comp_number = random.randrange(0, 2)
    comp_choice = number_to_name(comp_number)
    print(comp_choice)

    comp = -int(comp_number)
    play = int(number)
    diff = (comp + play) % 5

    if diff == 1 or diff == 3:
        print("You won!!!")
    elif diff == 0:
        print("Draw")
    elif diff == 2 or diff == 4:
        print("You lose!!!")
