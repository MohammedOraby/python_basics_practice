class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        if value < 0:
            raise ValueError("age must be positive")
        self.__age = value

Mohamed = Person("Mohamed Oraby",37)

print(Mohamed.age)

# Mohamed._saved_age = -1
# print(Mohamed.age)


# Sara = Person("Sara Mahmoud", -33)

# print(Sara.age)

# print(Mohamed.age)
# Mohamed.age = -37
# print(Mohamed.age)
