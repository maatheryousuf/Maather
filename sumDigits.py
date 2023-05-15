""" string, int """

dig = input("Enter a digit :")

def summ(d):
  a = 0
  for i in dig:
    i = int(i)
    a = a + i
  return a
    
result = summ(dig)
print (result)

""" int, string, int """

dig = int(input("Enter a digit :"))

def summ(d):
  t = str(dig)
  a = 0
  for i in t:
    i = int(i)
    a = a + i
  return a
    
result = summ(dig)
print (result)



