import json

with open("scores.json","r") as f:
    source = json.loads(f.read())

print(source)