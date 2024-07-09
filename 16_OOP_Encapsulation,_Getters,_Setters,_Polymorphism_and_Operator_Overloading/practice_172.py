## __gtt__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

Mohamed = Person("Mohamed",37)
Magdy = Person("Magdyy",33)
Nora = Person("Nora",30)


print(Mohamed > Magdy)