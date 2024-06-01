numbers = [22,33,44,55,66,77]

# convert list to string and join the to a string via list comprehension
s = " - ".join([str(number) for number in numbers])
print(s)