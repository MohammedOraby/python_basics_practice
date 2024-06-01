# def func1(**kwargs):
#     print(kwargs)
# func1(name1="ahmed",name2="nora",name3="mahmoud")

# def func2(**kwargs):
#     for _ in range(kwargs["times"]):
#         print(kwargs["name1"], kwargs["name2"], kwargs["name3"])

# func2(name1= "mohamed",name2= "sara",name3= "ali",times=4)

def func3(*args, **kwargs):
    
    # print(args)
    # print(kwargs)

    print(args[1])
    print(kwargs["edu"])

func3("mohamed",2.3,5,name="ali",age=33,edu="computer science")