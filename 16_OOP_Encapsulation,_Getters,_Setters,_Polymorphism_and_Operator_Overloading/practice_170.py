# Polymorphism: Operator Overloading

class Cash:
    def __init__(self,amount):
        self.amount = amount

    def __add__(self,other):
        return self.amount + other.amount
    
    def __str__(self) -> str:
        return f"{self.amount}$"
    

cash1 = Cash(100)
cash2 = Cash(200)

# cash3 = Cash("a")
# cash4 = Cash("b")

total = cash1+cash2
print(total)
print(type(total))


# print(cash3+cash4)
