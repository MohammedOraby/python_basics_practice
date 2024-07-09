# Inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print((f"{self.name} iis {self.age} yrs old"))

class Student(Person):
    def study(self): 
        print("i'm studying programming") 

    def print_info(self):
        print(f"hHi i'm a student {self.name}")

Mohamed = Student("Mohamed Oraby",22)

Mohamed.print_info()

