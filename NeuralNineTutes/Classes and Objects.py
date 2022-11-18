
class Person:

    people = 0 #class variable example

    def __init__(self, name, age, height): # constructor to make Person attributes
        self.name = name
        self.age = age
        self.height = height
        Person.people += 1

    def __del__(self): #this determens what happens when an object is deleted
        print("Object deleted:")
        Person.people -= 1

    def __str__(self): # string formatting to help understand the return(print) better
        return ("Name: {}, Age: {}, Height: {}". format(self.name, self.age, self.height))

print("*********************************************************************************")

person1 = Person("Mike", 30, 180) #making a variable person1 to pass the class attributes name, age, height
print(person1.name)
print(person1.age)
print(person1.height)

print("*********************************************************************************")

person2 = Person("Henery", 25, 180)
print(person2.name)
print(person2.age)
print(person2.height)

print("*********************************************************************************")
print("using str method using string formatting makes the print better") #using str function helps remove the need to print in multiple lines
print("*********************************************************************************")

person3 = Person("Sarah", 30, 180)
print(person3)

person4 = Person("Abraham", 25, 180)
print(person4)

print(Person.people)
