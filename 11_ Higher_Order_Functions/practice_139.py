## id() function --> returns the address in the memory where an object stored 
x = 600
y = 500
# z = int(500)

print(f"address of x :{id(x)}")
print(f"address of y: {id(y)}")
# print(f"address of z: {id(z)}")

print(x is y) ## is operator --> check if tp memory address is equals