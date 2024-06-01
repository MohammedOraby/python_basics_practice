products = ["cake","soda","chips"]
print("Enter product number")

try:
    index = int(input(" 0:cake -1:soda - 2:chips : "))
    print(f"Successfully ordered {products[index]}")
except (IndexError,ValueError):
    print("Invalid input")
finally:
    print("thank you come again")