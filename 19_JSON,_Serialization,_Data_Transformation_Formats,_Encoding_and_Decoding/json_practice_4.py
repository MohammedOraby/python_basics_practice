## strings inside json string must use double quote 

import json
json_string = '[null, true, "mohamed", 3.5]'

my_list = json.loads(json_string)
print(my_list)