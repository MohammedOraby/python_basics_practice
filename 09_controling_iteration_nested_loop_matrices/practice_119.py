## Short-Circuit Evaluation
usernames = ["mohamed","sara","ahmed"]
passwords = {"mohamed":"pass123","sara":"coffee11","ahmed":"ali11"}

username = input("enter username : ")
password = input("enter password : ")

def check_password():
    print("......") ## after proceed first condition
    return password == passwords[username]

if username in usernames and check_password():
    print ("welcome")
else:
    print("invalid username or password")

    