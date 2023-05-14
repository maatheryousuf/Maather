for r in range (1, 101):
    num = 0
    for c in range(1, r):
        if r % c == 0:
            num = num + c
    if num == r:      
        print (r)
