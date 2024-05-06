## replace values in variables 
x = 1
y = 2

original_x = x
x=y
y=original_x


print(x) 
print(y) 

## replace values in variables by tuples unpacking 

a = 5
b = 7 
a,b = b,a

print (a)
print (b)