__author__ = 'Louvie'

run = True

def fib(num):
    b = 1
    fib_list = [1]

    if num <= 0:
        print("You can't do that!")
        return

    elif num == 1:
        print(fib_list)
        return

    else:
        for i in range(1,num):
            fib_list.append(b)
            b = (fib_list[len(fib_list)-2]) + (fib_list[len(fib_list)-1])
            
    print(fib_list)





print("Give me a number and I will list a Fibbonacci Seq \n"
                "Press 'Q' to cancel:")

while run:
    ans = input()
    if ans == "Q" or ans == "q":
        run = False

    elif ans.isalpha():
        print("Invalid input.")

    else:
        try:
            ans = int(ans)
            fib(ans)

        except ValueError:
            print("There was a problem. Try again.")

