list = [22, 3, -2, -1, 10, 1]

product = 1
count = 0

for i in list:
    print (i, end =" , ")
    
    if i< 0:
        count += 1
    
    product = product * i
    
print()        
print("The total number of negative numbers in the list : ", count)
print("The product of list elements : ", product)

