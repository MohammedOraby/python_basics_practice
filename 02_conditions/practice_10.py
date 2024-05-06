cost =int ( input ("enter your purchases cost : ")[:-1])
delivery = 0
if cost >= 200 :
    cost -= cost*.2
elif cost < 100 :
    delivery = 15

print (f"cost : {cost}$")
print (f"delivery : {delivery}$")
print (f"total cost : {cost+delivery}$")
