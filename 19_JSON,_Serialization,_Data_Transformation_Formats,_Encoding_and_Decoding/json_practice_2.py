import json

x = '[true, 1, null]'

my_list = json.loads(x)
print(my_list)
for element in my_list:
    print(element , type(element))