# Bank acount :
    # first name , last name ,balance 
    # acount status : 
        # deactivate
        # activate    
    # withdraw 
    # deposit 
    # transfer
    # show account information 
    # show balance

class BankAccount:
    counter = 1

    def __init__(self,first_name,last_name,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.active = True
        self.acc_number = BankAccount.counter
        BankAccount.counter += 1

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def withdraw(self,amount):
        if self.active:
            if amount <= 0 or amount > self.balance:
                print("Invalid Transaction !!")  
            else:
                self.balance -= amount
        else:
            print("Inactivated account")
    
    def deposit(self,amount):
        if self.active:
            if amount <= 0:
                print("Invalid Transaction")
            else:
                self.balance += amount
        else:
            print("Inactivated account")
            

    def transfer(self,other,amount):
        if self.active and other.active and amount <= self.balance:
            self.balance -= amount
            other.balance += amount
        else:
            print("Invalid Transaction")

    def show_balance(self):
        print(f"{self.first_name}'s balance : {self.balance}$ ")

    # show account information
    def __str__(self): 
        full_name = f"{self.first_name} {self.last_name}"
        status = "Active" if self.active else "Inactive"
        return f"Name : {full_name.title()}.\nBalance : {self.balance}$\nAccount number : {self.acc_number}\nstatus : {status}"
    
mohamed = BankAccount("mohamed","oraby",500)
sara = BankAccount("sara","mahmoud",700)
ali = BankAccount("ali","hassan",400)

mohamed.show_balance()
sara.show_balance()
mohamed.deactivate()
# sara.deactivate()
# mohamed.deactivate()
mohamed.activate()
mohamed.transfer(sara,200)
mohamed.show_balance()
sara.show_balance()

# print(mohamed)
# print(sara)
# ali.deactivate()
# print(ali)

# mohamed.show_information()
# mohamed.deposit(-200)
# mohamed.deactivate()
# print(mohamed.acount_status)
# mohamed.activate()
# print(mohamed.acount_status)
# mohamed.deposit(100)
#mohamed.deposit(400)
# print(mohamed.balance)