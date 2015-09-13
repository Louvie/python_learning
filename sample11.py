__author__ = 'Louvie'


def first_last():
    run = True
    u_list = []
    print("Give me a list of whole numbers and I will give you a new one.\n"
          "Press 'ENTER' to enter a number.\n"
          "Press 'Q' to quit and see your result.")

    while run:
            ans = input()

            if ans.isnumeric():
                u_list.append(ans)

            elif ans == "Q" or ans == "q":
                run = False

            else:
                print("This is not a whole number. Try again.")


    if len(u_list) > 0:
        b = [u_list[0], u_list[len(u_list) - 1]]
        print(b)
    else:
        print("Nothing was entered.")

first_last()


