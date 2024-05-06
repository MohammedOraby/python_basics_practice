## initializing objects :
    ## special, dunder  (double underscore), magic or internal methods

class Employee:
    def __init__(self,name,salary,currency):
        self.name = name
        self.salary = salary
        self.currency = currency

    def print_info(self):
        print(f"name : {self.name} , salary : {self.salary}{self.currency}")

emp_1 = Employee("mohamed",900,"$")
emp_2 = Employee("sara",800,"$")
emp_3 = Employee(name="ali",salary=700,currency="YEN")

emp_1.print_info()
emp_2.print_info()
emp_3.print_info()