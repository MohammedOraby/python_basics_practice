## Decorators 

def print_mohamed():
    print("mohamed")

def print_sara():
    print("sara")

# def add_print_hi_statement(my_func):
#     print("hi")
#     my_func()

# # add_print_hi_statement(print_mohamed)
# add_print_hi_statement(print_sara)

def add_print_hi_statement_1(fn):
    def modified_fn():
        print("hi")
        fn()
    return modified_fn

modified_sara = add_print_hi_statement_1(print_sara)
modified_sara()