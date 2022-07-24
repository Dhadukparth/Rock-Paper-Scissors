# print("----------------------------------------------------------------------------------------------------")
import random

while True:
    role = ["rock", "paper", "scissors"]

    computer = random.choice(role)
    user = None

    print("--------------------------------------------------")
    while user not in role:
        user = input("rock, paper, scissors : ").lower()
    print("--------------------------------------------------")

    if user == computer:
        print("Computer : ",computer)
        print("User : ",user)
        print(" ------------------------ Tie ------------------------")

    elif user == "rock":
        if computer == "paper":
            print("Coumpter : ", computer)
            print("User : ", user)
            print(" ------------------------ You Lose! ------------------------")
        
        if computer == "scissors":
            print("Coumpter : ", computer)
            print("User : ", user)
            print(" ------------------------ You Win! ------------------------")

    elif user == "scissors":
        if computer == "paper":
            print("Coumpter : ", computer)
            print("User : ", user)
            print(" ------------------------ You Lose! ------------------------")
        
        if computer == "rock":
            print("Coumpter : ", computer)
            print("User : ", user)
            print(" ------------------------ You Win! ------------------------")

    exitgame = input("Play again game (Y/N) : ").lower()

    if exitgame == "y":
        break

print("Bye! thanks for play game")