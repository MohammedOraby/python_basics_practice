## print only strings in a list and skip integers

chars = ["a",2,"b",2,"c"]
for char in chars:
    if char == 2:
        continue
    print(char)