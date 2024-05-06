password = "abc"
balance = 1000
withdraw_amount = 150
if password !="abc" : 
    print ("unauthorized !")
elif withdraw_amount > balance :
    print ("insufficient funds !")
else :
    balance -= withdraw_amount 
    print (f"your current balance is {balance}$")