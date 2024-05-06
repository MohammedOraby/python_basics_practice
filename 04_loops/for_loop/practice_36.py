'''
product {product number} : {product name} status :
    - 0 expired 
    - 1 --> 7 "consume in # day(s)"
    - 7 > good
'''
products = ["milk","beef","fish","chicken","apple","cake","bread"]
day_to_expire = [7,30,0,15,1,-4,5]

for i in range (len(products)) :
    days_left = day_to_expire[i]
    if  days_left<= 0 :
        validity = "[Expired]"
    elif days_left <= 7 :
        validity = "consume in {day_to_expire[i]} day(s)"
    else :
        validity = "[Good]"
    print (f"Product {i} {products[i]} : {validity}")