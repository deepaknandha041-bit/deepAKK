import random
def game():
    user = input("Enter rock, paper or scissors: ")
    a = ("rock", "paper", "scissors")
    computer = random.choice(a)

    print("Computer chose:", computer)

    if user == computer:
        print("Tie!")
    elif (user == "rock" and computer == "scissors"):
        print("You win!")
    elif (user == "paper" and computer == "rock"):
        print("You loose!")
    elif (user == "scissors" and computer == "paper"):
        print("You win!")
    elif (computer == "rock" and user== "scissors"):
        print("You loose!")
    elif (computer == "paper" and user == "rock"):
        print("You loose!")
    elif (computer == "scissors" and user == "paper"):
        print("you loose!")
    else:
        print("Invalid input! Please enter rock, paper, or scissors.") 
    again = input("Do you want to play again? (yes/no): ")
    if again == "yes":
        game()  
game()