__author__ = 'Louvie'

####################################################################################
"""def reverse_add(word1, string1):
    word2 = ""
    for t in range(1, len(word1)+1):
        word2 = word2 + word1[len(word1) - t]

    string1 = string1 + word2
    return string1
"""
####################################################################################


s1 = input("Give me a anything and I will give it to you backwards!:")
#s1 = "Hello there! My name is Louvie"
s2 = ""
s1_list = s1.split()

for i in range(1, len(s1_list)+1):
    s2 = s2 + s1_list[len(s1_list) - i] + " "

####################################################################################
"""s2 = ""
word = ""
print(s1)

for i in range(1, len(s1) + 1):
    if s1[len(s1) - i] != " ":
        word = word + s1[len(s1) - i]

    else:
        s2 = reverse_add(word, s2) + " "
        word = ""

s2 = reverse_add(word, s2)
"""
####################################################################################
print(s2)
