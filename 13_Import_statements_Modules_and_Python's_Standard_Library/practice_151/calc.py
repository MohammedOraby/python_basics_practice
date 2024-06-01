print(__name__)

def square(x):
    return x**2

def cube(n):
    return n**3

def circle_area(r):
    return 3.14 * r**2

def rectangle_area(h,w):
    return w*h

# if __name__ == "__main__":
#     if square(2) == 4:
#         print("the square function running successfully")
#     print("this rub uf module run directly")

# else:
#     print("this run if module imported (run un directly)")

def check_script():
    if __name__ == "__main__":
        if square(2) == 4:
            print("the square function running successfully")
        print("this run uf module run directly")

    else:
        print("this run if module imported (run un directly)")

check_script()