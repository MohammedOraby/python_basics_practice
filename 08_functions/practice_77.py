def my_func ():
    n = int(input("enter a number : "))
    print (f"{n} squared : {n**2}")

times = int(input("how many time you rant to play : "))
for time in range(times) :
    my_func()