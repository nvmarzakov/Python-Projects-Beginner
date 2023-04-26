import random
from colorama import Fore, Back, Style

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

choose_yes_or_no = ""

while True:
    if choose_yes_or_no == "no":
        print("Thank you for playing!")
        break

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
        print("You choose Rock")
    elif player_move == "p":
        player_move = paper
        print("You choose Paper")
    elif player_move == "s":
        player_move = scissors
        print("You choose Scissors")
    else:
        raise SystemExit("Invalid Input. Try again")

    computer_random_number = random.randint(1, 3)
    computer_move = ""


    if computer_random_number == 1:
        computer_move = rock
        print("The computer choose Rock")
    elif computer_random_number == 2:
        computer_move = paper
        print("The computer choose Paper")
    else:
        computer_move = scissors
        print("The computer choose Scissors")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        print(Fore.LIGHTYELLOW_EX + "Draw")
    else:
        print(Fore.RED + "You lose!")

    choose_yes_or_no = input(Fore.RESET + "Type [yes] to Play Again or [no] to quit: ")
    if choose_yes_or_no != "yes" and choose_yes_or_no != "no":
        raise SystemExit(Fore.RED + "You choose invalid word. Please start the game again!")
