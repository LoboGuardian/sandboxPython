import random

# Creating a list of play options
hands = ["Rock", "Paper", "Scissors"]

while True:
    # Assign a random play to the computer
    computer = random.choice(hands)

    # Get player's input
    player = input("Rock, Paper, Scissors?: ").capitalize()

    if player not in hands:
        print("That's not a valid play. Check your spelling!")
        continue

    if player == computer:
        print("Tie!")
    elif player == "Rock" and computer == "Paper":
        print("You lose!", computer, "covers", player)
    elif player == "Rock" and computer == "Scissors":
        print("You win!", player, "smashes", computer)
    elif player == "Paper" and computer == "Scissors":
        print("You lose!", computer, "cut", player)
    elif player == "Paper" and computer == "Rock":
        print("You win!", player, "covers", computer)
    elif player == "Scissors" and computer == "Rock":
        print("You lose!", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)