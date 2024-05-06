## get max 

def get_max (x,y,z,m) :
    collection = [x,y,z,m] 
    maximum = collection[0]
    for num in collection : 
        if num > maximum :
            maximum = num
    return maximum
print(get_max(33,-1,6,122))