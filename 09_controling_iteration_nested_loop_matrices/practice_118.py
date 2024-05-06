## Short-Circuit Evaluation
usernames = ["mohamed","sara","ahmed"]
passwords = {"mohamed":"pass123","sara":"coffee11","ahmed":"ali11"}

username = input("enter username : ")
password = input("enter password : ")
if username in usernames and password == passwords[username]:
    print("welcome ...")
else:
    print("invalid username or password")