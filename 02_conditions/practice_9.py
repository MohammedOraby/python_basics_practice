purchases = input ("enter your purchases value :")
discount = int(purchases[:-1]) * .15
if int(purchases[:-1]) < 100 :
    print (f"your purchases cost is {purchases[:-1]}$")
    print(f"your delivery cost is 15$")
    print(f"your total cost {int(purchases[:-1])+15}$") 

elif int(purchases[:-1]) >= 100  > 200 :
    print (f"your purchases cost is {purchases[:-1]}$")
    print(f"your delivery cost is 0$")
    print(f"your total cost {purchases[:-1]}$") 

else : 
    print (f"your purchases cost is {purchases[:-1]}$")
    print(f"your delivery cost is 0$")
    print (f"you got discount {int(purchases[:-1])-discount}$")
    print(f"your total cost {int(purchases[:-1])+15}$") 


