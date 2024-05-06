passwords = ["p@w00rd","strongerpass","123"]
for password in passwords : 
    if len(password) > 6 :
        print (f"{password} is strong")
    else :
        print (f"{password} is to short ")