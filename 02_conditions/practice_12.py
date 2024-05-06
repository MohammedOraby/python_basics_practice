pizza_type = input ("Chicken or Beef (C/B) : ").upper()
s = 7
m = 12
l = 18
inc = 0
if pizza_type == "C" :
    pizza_type = "Chicken"
elif pizza_type == "B" :
    pizza_type = "Beef"
    inc = 1

pizza_size = input (f"small {s+inc}$ , medium {m+inc}$ or large {l+inc}$ (S/M.L) : ").upper()

if pizza_size == "S" :
    pizza_size ="small"
    price = s+inc 
elif pizza_size == "M" :
    pizza_size ="medium"
    price = m+inc
elif pizza_size == "L" :
    pizza_size ="large"
    price = l+inc

extra = input ("extra cheese (Y/N) : ").upper()
if extra == "Y" :
    extra = "with extra cheese"
    price += 2
elif extra == "N" : 
    extra = ""

print ("Order summary : ")
print (f"{pizza_size} {pizza_type} Pizza {extra}")
print (f"Total price : {price}$")