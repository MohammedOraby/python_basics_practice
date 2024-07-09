# Abstraction :
    # Hiding implementation details
    # Caring about what something does , Not how it does it (coffee machine)

from abc import ABC, abstractmethod

class Shape(ABC): # Abstract base class
    @abstractmethod
    def area(self):
        pass  

class Circle(Shape): # Concrete class  
    def __init__(self, radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius**2
        

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Triangle(Shape):
    def __init__(self, height, base_width):
        self.height = height
        self.base_width = base_width

    def area(self):
        return 0.5 * self.height * self.base_width

c1 = Circle(.5)
r1 = Rectangle(2,5)
t1 = Triangle(4,2)

# print(c1.area())
# print(r1.area())
# print(t1.area())


for shape in [c1, r1, t1]:
    print(shape.area())