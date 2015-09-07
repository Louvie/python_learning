__author__ = 'Louvie'
import random
game = True
guess = 0

while game:
    ans = random.randint(1, 9)
    num = input("I'm thinking of a number between 1 and 9. Guess!:")
    guess+= 1

    if not num.isnumeric():
        print("Do you even want to play?")

    else:
        num = int(num)
        while num != ans:
            if num < 1 or num > 9:
                num = int(input("That is not valid! Try again:"))
                guess += 1

            else: #num >= 1 and num <= 9:
                if num < ans:
                    num = int(input("Too low. Try Again:"))
                else:
                    num = int(input("Too high. Try Again:"))
                guess+= 1

        print("You got it! It took you %d guesses" % (guess))

    guess = 0
    choice = input("Continue? (Y/N):")
    if choice.lower() == "n":
        game = False


