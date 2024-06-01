balance = 500
transfer_count = 0

def transfer_actions(fn):
    def modified_fn():
        global transfer_count
        fn()
        transfer_count +=1
    return modified_fn

@transfer_actions
def withdraw_ten():
    global balance
    balance -= 10

@transfer_actions
def withdraw_fifty():
    global balance
    balance -= 50

@transfer_actions
def withdraw_hundred():
    global balance
    balance -= 100

withdraw_ten()
withdraw_fifty()
withdraw_hundred()

print(balance)
print(transfer_count)
