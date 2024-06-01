products = ["cake","soda","chips"]
print("Enter product number")
index = int(input(" 0:cake -1:soda - 2:chips : "))


try:
    print(f"Successfully ordered {products[index]}")
except IndexError:
    print("Invalid input")