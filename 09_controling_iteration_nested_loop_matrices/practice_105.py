# while True:
#     height = int(input("enter height (>=10 , 0> ) : "))
#     cols = 1
#     if height > 0 and height <= 10:
#         break
#     else:
#         continue

# for _ in range(height):
#     for _ in range(cols):
#         print("*",end="")
#     print()
#     cols +=1


while True:
    height = int(input("enter height (>=10 , 0> ) : "))
    if height > 0 and height <= 10:
        break

# for i in range(height):
#     for _ in range(i+1):
#         print("*",end="")
#     print()

for i in range(height):
    print("*"*(i+1))
    
