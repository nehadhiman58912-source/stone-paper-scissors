from game import game
if __name__ == "__main__":
    while True:
        game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break