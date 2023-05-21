class Person:
    no_of_person = 0
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age
        Person.no_of_person +=1
        
        
    def __str__(self) :
        return "This person name is {} and {} years old".format(self.name, self.__age)    

    def set_age(self, new_age):
        self.__age = new_age
"""the __ before age mrans the age variable became private"""        

p1 = Person("Maather", 23)
p2 = Person("Rana", 4)
p3 = Person("Asim", 11)

'''print(p1.__str__())'''
'''print(p2.__str__())'''
'''print(p3.__str__())'''
'''print(Person.no_of_person)'''
"""print(dir(Person))"""

p2.set_age(27)
print(p2.__str__())
p2.__age= 5
print(p2.__str__())
