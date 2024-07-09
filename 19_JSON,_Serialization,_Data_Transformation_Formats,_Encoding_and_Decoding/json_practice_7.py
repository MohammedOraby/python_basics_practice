import json

my_dict = {
    "name":"sara",
    "friends":("fatema","mariam","hasnaa")
}

json_string = json.dumps(my_dict,indent=2)
print(json_string)