def func1():
    print("hi")

    def func2():
        print("bye")
    return func2

x = func1()
x()