# def func(*x):
#     print(x)
# func(1,2,3,4)

# def add(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     print(total)

# add(2,3,4,5,6)

def my_func(x,y,*args):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"args: {args}")

my_func(44,55,66,77,88,99)