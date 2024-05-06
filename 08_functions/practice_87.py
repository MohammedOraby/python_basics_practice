'''
1-func to return length ("ahmed")
2-func to return length ([3,5,2.7,"a"])
3-func to return length (("m",3,[2,5,"l"]))
4-func to return length ({654})
6-func to return length ([])
'''
 
def get_length(x):
    count = 0
    for char in x :
        count+=1
    return count
print(get_length("ahmed"))
print(get_length([3,5,2.7,"a"]))
print(get_length(("m",3,[2,5,"l"])))
print(get_length({654}))
print(get_length([]))



