## common misconception regarding dynamic code
## important Note : python will not re evaluate an expression has ended its evaluation

fruits = ["apple","banana","orang"]
people = ["ahmed","ali"]

dict_1 = {"fruits_count":len(fruits),
          "people_count":len(people)}

print(dict_1)

fruits = ["grape"]
people = ["sara","mohamed"]

print(dict_1)