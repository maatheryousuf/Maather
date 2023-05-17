rows = int(input("Enter number of rows:"))
col = int(input("Enter number of columns:"))

t = [[i]*col for i in range(rows)]

for i in range(rows):
    for j in range (col):
         t[i][j] = int (input("Enter a number :"))
print(t)
print() 

t = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        if i == j:
           t[i][j]=1
        elif i>j :
           t[i][j]=2

for i in range (4):
    for j in range(4):
        print(t[i][j], end = '   ')
    print() 




print()
t = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        if (i+j)% 2 == 0 :
           t[i][j]=1

for i in range (4):
    for j in range(4):
        print(t[i][j], end = '   ')
    print()
   
