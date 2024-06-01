# lambda function 

def calc(s):
    if s == "add":
        return lambda x, y: x+y
    elif s == "multiply":
        return lambda x, y: x*y
    elif s == "divide":
        return lambda x, y: x/y

addition = calc("add")
print(addition(8,2))

multi = calc("multiply")
print(multi(8,2))

divide = calc("divide")
print(divide(8,2))