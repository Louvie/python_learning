__author__ = 'Louvie'

run = True

my_list = []

print("Give me a list of anything and I will give you one without duplicates!\n"
      "Type in '\q' to see the result.")
while run:
    ans = input()
    if ans == "\q" or ans == "\Q":
        run = False
    else:
        my_list.append(ans)

print("Here it is!\n")
print(set(my_list))
