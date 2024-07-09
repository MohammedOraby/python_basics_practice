import json

x = [1, None, True]
json_string = json.dumps(x)

print(json_string)
print(type(json_string))