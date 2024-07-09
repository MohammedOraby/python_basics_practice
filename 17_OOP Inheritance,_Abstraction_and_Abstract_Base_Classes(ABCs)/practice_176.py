# Inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print((f"{self.name} iis {self.age} yrs old"))

class Student(Person):
    def __init__(self, name, age, university):
        # call __init__ of Person class 
        super().__init__(name, age) # Person.__init__(self,name,age)
        self.university = university

Mohamed = Student("Mohamed Oraby",37,"MIT")

print(Mohamed.name)
print(Mohamed.age)
print(Mohamed.university)

