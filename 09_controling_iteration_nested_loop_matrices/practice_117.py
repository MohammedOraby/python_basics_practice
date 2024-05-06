## check username

# username = "mohamed"
# if len(username) > 2 \
# and len(username) < 10 \
# and "$" not in username \
# and "#" not in username:
#     print("valid username")

# else:
#     print("invalid")

def valid_username(username):
    return len(username) > 2 \
        and len(username) < 10 \
        and "$" not in username \
        and "#" not in username

username = input("enter username : ") 
if valid_username(username):
    print("valid username")
    
else:
    print("invalid")