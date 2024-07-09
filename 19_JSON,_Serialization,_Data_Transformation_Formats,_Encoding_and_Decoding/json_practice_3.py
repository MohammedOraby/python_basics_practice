# (encoding) list, tuple -->> array
# (decoding) array ---> list


import json

x = (1,2,3)
json_string = json.dumps(x)
print(json_string)