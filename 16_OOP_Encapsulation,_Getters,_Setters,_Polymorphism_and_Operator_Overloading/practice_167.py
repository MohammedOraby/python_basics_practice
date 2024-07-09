class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter  
    def radius(self, value):
        if value <= 0:
            raise ValueError("value must be positive")  
        self.__radius = value

c = Circle(5)
# c.radius = -10
c.radius = 8
print(c.radius)