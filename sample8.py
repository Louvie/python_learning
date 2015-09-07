__author__ = 'Louvie'
import random

game = True

while game:
    print("Let's play Rock, Paper, Scissors!")
    choice = input("Rock = 1 \nPaper = 2 \nScissors = 3 \nWhich one?:")
    if not choice.isnumeric():
        print("Not a number! \n")

    else:
        choice = int(choice)
        if choice > 0 and choice < 4:
            opponent = random.randint(1, 3)
            print(opponent)

            if choice == opponent:
                print("TIE! \n")
            elif (choice == 1 and opponent == 2) or (choice == 2 and opponent == 3) or (choice == 3 and opponent == 1):
                print("You Lost!\n")
            else:
                print("You Win!\n")
        else:
            print("Not a valid choice!\n")

    cont = input("Play again? (Y/N):")

    if cont.lower() == "n":
        game = False
