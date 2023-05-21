
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

