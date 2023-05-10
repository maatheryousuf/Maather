import math
word = input("write a word:")

middle_Char = word[(len(word)-1)//2:(len(word)+2)//2]
print("The original word", word)
print("The middlle characters", middle_Char)
