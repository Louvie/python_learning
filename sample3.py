__author__ = 'Louvie'
stop = int(input("Give me a roof number:"))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for spot in a:
    if spot < stop:
        b.append(spot)


print(b)
