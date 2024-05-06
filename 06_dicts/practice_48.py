## dict keys ban only be string , float ,int or tuple

student = {"id":1234,"name":"mohamed","age":34,"major":"physics"}
# print (student["name"]) ##retrieving ,locking up ,accessing or getting a value 
# print (len(student)) 
# print(student["age"]+5)
# print(student["name"].upper())
x = input("user info : ")
print (student[x])
