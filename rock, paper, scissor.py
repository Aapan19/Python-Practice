import random

options = ("rock", "paper", "scissors")

running = True

while running:
    print()
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice from (rock, paper or scissors): ")

    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie! ")
    elif player == "rock" and computer == "scissors":
        print("Hurray! You Win! ")
    elif player == "paper" and computer == "rock":
        print("Hurray! You Win! ")
    elif player == "scissors" and computer == "paper":
        print("Hurray! You Win! ")
    else:
        print("Sorry! You loss the game! ")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

    # play_again = input("Play again? (y/n): ").lower()
    # if not play_again == "y":
    #     running = False

print("Thanks for Playing")

# if not input("Play again? (y/n): ").lower() == "y":
#     running = False
