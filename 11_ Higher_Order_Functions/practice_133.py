# x = "mohamed" ## global variable 
# def func_1():
#     print(x)
# func_1()


def func_1():
    y = "ahmed" # y is local variable for fun_2
    def func_2():
        nonlocal y 
        y = "ali" # change variable y value in fun_2 by nonlocal statement
        print("y in func_2" ,y) # y is (nonlocal) variable for func_3
    func_2()
    print("y in func_1" ,y)
func_1()