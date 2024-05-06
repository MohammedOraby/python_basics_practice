def func():
    numbers = [1,2,3,4,5]
    for number in numbers :
        print(number)
        if number == 3:
            return
        print("hi")

    print("outside the loop")
func()

def func1():
    numbers = [1,2,3,4,5]
    for number in numbers :
        print(number)
        if number == 3:
            break
        print("hi")

    print("outside the loop")
func1()