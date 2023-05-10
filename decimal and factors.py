
word = input("Enter:")

c = 0

while (c <=6):
     print (ord(word[c]))
     c += 1
     



number = int(input("Enter any number:"))
factors =[]
for t in range(1, number+1):
    
    if number % t ==0:
        factors.append(t)
   
    
for f in factors :
    print(f)    