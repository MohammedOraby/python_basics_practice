import json

with open("data.txt") as f :
    data = f.read()

result = json.loads(data)
# print(result)
print(result["name"])
print(type(result))