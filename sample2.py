__author__ = 'Louvie'
################################################################################################
#number = int(input("Give me a number and I can tell you if it is even or not:\n"))

#if number % 2 == 0:
#    print("Yep!")
#    if number % 4 == 0:
#        print("And it's a multiple of 4!")

#else:
#    print("Engh Engh!")
################################################################################################

num = int(input("How about a number:"))
div = int(input("And another:"))

if num % div == 0:
    print(str(div) + " divides nicely into " + str(num) + "!")

else:
    print("Sorry. There is no even division...Good bye!")
