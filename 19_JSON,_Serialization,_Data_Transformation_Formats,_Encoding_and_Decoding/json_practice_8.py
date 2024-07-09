import json

json_string = '''{
"book":"introduction to algorithms",
"reviews":{"mohamed":"very good","sara":"excellent"}
}'''

my_dict = json.loads(json_string)
print(type(my_dict))
print(my_dict["reviews"]["sara"])