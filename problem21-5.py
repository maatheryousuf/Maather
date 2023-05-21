"""Print the number with the highest number of repeating elements"""
numbers = [1,8,7,4,1,2,2,2]

counter = 0
highest_number = 0

for i in numbers:
    dup = numbers.count(i)
    if dup > counter :
        counter = dup
        highest_number = i

print("The original list ",numbers)      
print("The number with the highest number of repeating elements is ",highest_number)


"""Print all numbers that have duplicates numbers"""

numbers = [1,8,7,4,1,2,2,2]
listt = []


for i in numbers:
    s = numbers.count(i)
    if s >1 :
        if listt.count(i) == 0:
            listt.append(i)
        
print("The total number of elements that has duplicate numbers",i)
print("The original list ",numbers)
print("The new list for numbers that have duplicates",listt)




