__author__ = 'Louvie'

run = True

def isPrime():
    try:
        num = int(input("Give me a number and let's see if it is a prime: " ))

        stopper = int(num/2) +1
        prime = False


        a = range(2, stopper)

        for i in a:
            if num % i == 0:
                prime = True
                break
            else:
                pass


        if prime:
            print("This is not a prime.")
        else:
            print("This is a prime.")

    except ValueError:
        print("Invalid input!")


while run:
    isPrime()
    ans = input("Play again? (Y/N)")
    if ans == "N" or ans == "n":
        run = False
