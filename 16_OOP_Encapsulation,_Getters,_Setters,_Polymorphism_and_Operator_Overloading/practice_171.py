# Polymorphism: Operator Overloading

class Cash:
    def __init__(self,amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self,other):
        if self.currency != other.currency:
            raise ValueError("can not add money of different currency")
        return Cash(self.amount + other.amount,self.currency)
    
    def __str__(self):
        return f"{self.amount}{self.currency}"
    

cash1 = Cash(100,"$")
cash2 = Cash(200,"$")
cash3 = Cash(200,"EUR")

total = cash1 + cash2
print(total)
print(total.amount)
print(type(total))
