class Person:
    
  def __init__(self):
     self.stack = []
        
  def push(self, name):
      for i in str(name):
          self.stack.append(i)

  def pop(self):
     for i in range(7):
        print(self.stack.pop())
    
p = Person()
p.push("Maather")
print(p.stack)
p.pop()       
print(p.stack)