a = [1, 2,7,5,8,2,1]
for i in range(len(a)):
    c = a.count(a[i])
    if c == 1:
        print(a[i])
        break
    