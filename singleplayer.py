import random
user = input("Enter a choice (rock, paper scissors): ")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
print(f"\nYou chose {user}, computer chose {computer}.\n")
if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else: print("Invalid input")