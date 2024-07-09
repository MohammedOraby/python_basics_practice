import json

json_string = '''[
    {"name":"mohamed","age":37},
    {"name":"sara","age":33},
    {"name":"ali","age":31}
]'''

result = json.loads(json_string)
for person in result:
    print(person["name"])