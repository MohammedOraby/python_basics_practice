try:
    x = int(input("enter a number : "))

except ValueError: # ValueError --> if user enter a letter
    print("invalid input")

print(x) # if user enter letter x will not define