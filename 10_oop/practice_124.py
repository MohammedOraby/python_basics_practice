class Employee:
    def __init__(self,name,salary,currency):
        self.name = name
        self.salary = salary
        self.currency = currency
        # self.info = f"name : {self.name} , salary : {self.salary}{self.currency}"

    def rase_salary(self,rase):
        self.salary = self.salary + (self.salary*rase/100)

    # def print_info(self):
    #     print(f"name : {self.name} , salary : {self.salary}{self.currency}")

    def __str__(self):
        return f"name : {self.name} , salary : {self.salary}{self.currency}"

mohamed = Employee("mohamed",1000,"$")
mohamed.rase_salary(10)
# emp_1.print_info()
print(mohamed)
# print(emp_1.info)

# emp_2 = Employee("ahmed",800,"SR")
# print(emp_2.info)
