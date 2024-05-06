class Employee:
    pass 

emp_1 = Employee()
emp_1.name = "mohamed"
emp_1.salary = 500
emp_1.currency = "$"

# print(emp_1.name)
# emp_1.salary = 700
# print(emp_1.salary)
# emp_1.salary += 50
# print(emp_1.salary)

emp_2 = Employee()
emp_2.name = "sara"
emp_2.salary = 700
emp_2.currency = "SR"

def print_info(emp):
    print(f"name : {emp.name} , salary : {emp.salary}{emp.currency}")
print_info(emp_1)
print_info(emp_2)