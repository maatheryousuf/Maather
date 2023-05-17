a = {True, "Maather", ('rana', 'asim'), 1}
b = {True,0 ,False}
b.update([2, 7, 'Rana', 6])
b.update('Suhaila')
print(b)


m = [[1,2,3],
     [5,7,8]]

for i in range(2):
    for j in range(3):
        print(m[i][j], end = '  ')
    print()
