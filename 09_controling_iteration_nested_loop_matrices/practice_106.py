my_list = [
    [1,2,3],
    ["a",True,1.6],
    [6,8],
    ["hello","a",5,False]
]

for nested_list in my_list:
    for element in range(len(nested_list)):
        nested_list[element] = 0
print(my_list)