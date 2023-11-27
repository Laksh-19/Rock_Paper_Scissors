import random
while True:
    choices=['rock','paper','scissors']
    computer=random.choice(choices)
    player=input("rock, paper or scissors?: ").lower()
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("Your choice: "+player)
        print("Computer's choice: " + computer)
        print("It is a Tie!")

    elif player=='rock':
        if computer =='paper':
            print("Your choice: " + player)
            print("Computer's choice: " + computer)
            print("You lost!")
        if computer == 'scissors':
            print("Your choice: " + player)
            print("Computer's choice: " + computer)
            print("You Won!")

    elif player=='paper':
        if computer =='scissors':
            print("Your choice: " + player)
            print("Computer's choice: " + computer)
            print("You lost!")
        if computer == 'rock':
            print("Your choice: " + player)
            print("Computer's choice: " + computer)
            print("You Won!")

    elif player=='scissors':
        if computer =='rock':
            print("Your choice: " + player)
            print("Computer's choice: " + computer)
            print("You lost!")
        if computer == 'paper':
            print("Your choice: " + player)
            print("Computer's choice: " + computer)
            print("You Won!")

    play_again=input("Wanna play again?: (yes/no) ").lower()
    if play_again != "yes":
         break
print("Bye!")



