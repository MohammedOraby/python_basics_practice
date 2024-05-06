## mutating with iterating 

# list_1 = [1,2,3,4]
# list_2 = [2,3,]
# for number in list_1 : 
#     if number in list_2 :
#         list_1.remove(number)
# print (list_1)

## write solution 

list_1 = [1,2,3,4]
list_2 = [2,3,]
for number in list_1[:] : 
    if number in list_2 :
        list_1.remove(number)
print (list_1)