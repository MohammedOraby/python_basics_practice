def square_area(num):
    if num < 0:
        ## create custom error
        raise ValueError("side length must be non-negative")
    else:
        return num*num
    
side_length = float(input("enter the side length : "))
print(square_area(side_length))