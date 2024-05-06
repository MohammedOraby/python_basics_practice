x = 10

def f():
    global x
    x = 50 
    print(x)

f()
print(x)