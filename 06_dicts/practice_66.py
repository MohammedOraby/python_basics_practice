dict_1 = {"name":"mohamed","age":39,"gpa":3.4}

## return keys
# for k in dict_1 : 
#     print(k)

## by key() method --> the same if we don't use this method 
# for k in dict_1.keys():
#     print(k)

## return values
# for v in dict_1 : 
#     print(dict_1[v])

## value() method --> return  value
# for v in dict_1.values() : 
#     print(v)

## items() method --> return tuple for every (key & value)
for item in dict_1.items() : 
    print(item)