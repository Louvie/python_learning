__author__ = 'Louvie'

testWord = input("Type a word and let's see if it is a palindrome: ")

orig, rev = [], []

for c in testWord:
    orig.append(c)
    rev.append(c)

rev.reverse()


if orig == rev:
    print("PALIDROME!")

else:
    print("NOPE!")

print(orig)
print(rev)
