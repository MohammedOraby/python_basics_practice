## json in multiline 

import json

json_string = '''{
    "name":"mohamed",
    "friends":["ahmed","aly"]
}'''

x = json.loads(json_string)
print(x)


