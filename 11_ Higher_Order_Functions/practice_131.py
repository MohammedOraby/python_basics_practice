## write a calculator function :
    # tak 2 arguments and function
    # perform the specified calculation and return the result
# define add. subtract, multiply, divide functions

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calculate(x,y,func):
    return func(x,y)

print(calculate(8,4,add))
print(calculate(8,4,subtract))
print(calculate(8,4,multiply))
print(calculate(8,4,divide))



