# students_grades = [("ahmed",77),("mohamed",88),("sara",99)]
# for x in students_grades :
#     print (f"student : {x[0]} - grade : {x[1]}")


## with unpacking 
# students_grades = [("ahmed",77),("mohamed",88),("sara",99)]
# for x in students_grades :
#     name , grade = x 
#     print (f"name : {name} -- grade : {grade}")

students_grades = [("ahmed",77),("mohamed",88),("sara",99)]
for name,grade in students_grades :
    print (f"name : {name} -- grade : {grade}")