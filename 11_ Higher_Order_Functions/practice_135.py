# Parameters and Closures

def func_1(n):
    def func_2():
        print(n)
    return func_2
x = func_1(10)
x()