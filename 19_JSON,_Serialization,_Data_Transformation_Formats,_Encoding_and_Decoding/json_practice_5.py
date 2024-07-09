# (python) dict <---> object (json)

import json
my_dict = {"name":"mohamed","age":37}

json_string = json.dumps(my_dict)
print(json_string)