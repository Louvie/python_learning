__author__ = 'Louvie'
num = int(input("Give me a number and I will tell you the divisors:"))

a = range(1,num+1)

for obj in a:
    if num % obj == 0:
        print(obj)
