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
    pass 

Ali = Student("Ali Mohamed",22)

Ali.print_info()