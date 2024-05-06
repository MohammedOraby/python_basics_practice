def is_member (item , collection) :
    for i in collection :
        if i == item :
            return True

    return False 

print(is_member("a",[1,4,"a","m"]))
print(is_member(9,[1,4,"a","m"]))