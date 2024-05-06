n = int(input("enter a number : "))
total = 0
for number in range (1,n+1):
    if number%2 == 0 :
        total += number
print (f"sum of even number from 1 to {n} is {total}")
