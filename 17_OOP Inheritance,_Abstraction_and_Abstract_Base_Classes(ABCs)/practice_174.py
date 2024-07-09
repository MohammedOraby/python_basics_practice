# Inheritance

# parent / superclass / base
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # child / subclass /derived
    def print_info(self):
        print((f"{self.name} iis {self.age} yrs old"))

class Student(Person):
    def study(self): # add methods to a child class -->> class extension (Student extend Person)
        print("i'm studying programming") 

Ali = Student("Ali Mohamed",22)

Ali.print_info()
Ali.study()
