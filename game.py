import random
def game():
    CHOICES=["stone", "paper", "scissors"]
    user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
    if user_choice not in CHOICES:
        print("Invalid choice.")
        return
    computer = random.choice(CHOICES)
    print(f"Computer chose: {computer}")
    if user_choice == computer:
        print("It's a tie!")
    elif (user_choice == "stone" and computer == "scissors") or\
          (user_choice == "paper" and computer == "stone") or\
              (user_choice == "scissors" and computer == "paper"):
        print("You win!") 
    else:
        print("Computer wins!")
game()