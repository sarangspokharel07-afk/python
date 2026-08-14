import random

#--banner--
print("*"*30)
print("ROCK- PAPER- SCISSORS")
print("*"*30)

#---SETUP---
choices=("rock", "paper", "scissors")
beats={
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
score={"player": 0, "computer": 0, "ties": 0}

#---game loop---
playing=True
while playing:
    #---player choice---
    player_choice=input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    #---computer choice---
    computer_choice=random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    #---determine winner---
    if player_choice == computer_choice:
        print("It's a tie!")
        score["ties"] += 1
    elif beats[player_choice] == computer_choice:
        print("You win!")
        score["player"] += 1
    else:
        print("Computer wins!")
        score["computer"] += 1

    #---display score---
    print(f"Score: Player {score['player']} - Computer {score['computer']} - Ties {score['ties']}")

    #---play again---
    play_again=input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        playing=False
        print("Thanks for playing!")