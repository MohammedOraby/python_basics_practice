def greeting():
    print("hi")
    print("hello")

def func(y):
    print("mohamed")
    # y = greeting() 
    y()
    print("ahmed")

# func(greeting())
func(greeting)
