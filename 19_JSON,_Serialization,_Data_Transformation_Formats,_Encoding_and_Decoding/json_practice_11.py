import json


people = [
    {"name":"Mohamed","married":True,"partner":"Sara"},
    {"name":"Ahmed","married":False,"partner":None}
]

with open("people.json","w") as f:
    f.write(json.dumps(people,indent=2))