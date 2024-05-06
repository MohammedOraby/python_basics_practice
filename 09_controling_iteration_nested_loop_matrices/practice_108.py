while True:
    n = int(input("height : "))
    if 0 < n <= 8:
        break

for i in range(n):
    for j in range(n):
        if i + j + 1 >= n :
            print( "*",end="")
        else:
            print(" ",end="")

    print()