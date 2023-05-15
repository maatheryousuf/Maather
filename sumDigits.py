dig = input("Enter a digit :")

def summ(d):
  a = 0
  for i in dig:
    i = int(i)
    a = a + i
  return a
    
result = summ(dig)
print (result)


