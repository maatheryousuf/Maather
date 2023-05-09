n1= int(input("Enter number 1="))
n2= int(input("Enter number 2="))
n3= int(input("Enter number 3="))
        
numbers=[n1, n2, n3]

if numbers[0]== numbers[1]== numbers[2]:
        print ("They are equal")
else:
        print("The biggest number is", max(numbers))
