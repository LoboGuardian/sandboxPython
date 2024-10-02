import random

# Setting min a max values for the dice
min_value = 1
max_value = 6

while True:
    print("Rolling dice...")
    print("The numbers are..")
    print(random.randint(min_value, max_value))
    print(random.randint(min_value, max_value))

    play_again = input("\nRoll dice again? (yes/no): ").lower()
    if play_again not in ("yes", "y"):
        break