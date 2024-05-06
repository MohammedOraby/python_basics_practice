## get sequence of number 

def get_sequence_num (n) :
    if n < 0 :
        sign = -1
    else : 
        sign = 1
    n = sign * n
    total = 0 
    for i in range (n+1):
        total += i 

    if sign == -1 :
        total = total * -1

    return total

print(get_sequence_num(400))
print(get_sequence_num(-250))

