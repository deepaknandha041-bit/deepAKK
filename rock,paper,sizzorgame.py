import random

def game():
    user = input("Enter rock, paper or scissors: ")
    a = ("rock", "paper", "scissors")
    computer = random.choice(a)

    print("Computer chose:", computer)

    if user == computer:
        print("Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    again = input("Do you want to play again? (yes/no): ")
    if again.lower() == "yes":
        game() 
game()
