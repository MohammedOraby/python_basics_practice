# Closures : is a function + it's environment (it's surrounding)
    # function + the information needed to work

# def func_1():
#     x = 10
#     def func_2():
#         print(x)
    
#     return func_2 # return value for func_1
# y = func_1() ## keeps fuc_2 as value for func_1
# y() # python keeps the needed info surround func_2 to work (closures)  

# Parameters and Closures
def my_func_1(n):
    def my_func_2():
        print(n)
    return my_func_2
z = my_func_1(5)
z()