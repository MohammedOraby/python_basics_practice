def func () :
    hobbies = {"mohamed":"ping pong","sara":"reading","ali":"football"}
    return hobbies
for name , hobby in func().items() : ## for loop header will execute once
    print (f"{name} - hobby : {hobby}") ## print statement will execute depending on loop iterations 
