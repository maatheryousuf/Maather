m = [[1,2,3],
     [5,7,8]]
total = 0
for i in range(2):
    for j in range(3):
        total += m[i][j]


print(total)
total = 0
for i in range(2):
        total += m[i][0]

print(total)
total = 0
for j in range(3):
        total += m[1][j]

print(total)



b = [[i]*3 for i in range (1,4)]
print(b)


for i in range (3):
    for j in range(3):
        print (b[i][j], end = '   ')
    print ()