class Employee:
    def print_info(self):
        print(f"name : {self.name} , salary : {self.salary}{self.currency}")

    def add_info(self,given_name,given_salary,given_currency):
        self.name = given_name
        self.salary = given_salary
        self.currency = given_currency



emp_1 = Employee()
emp_1.add_info("mohamed",700,"USD")
emp_1.print_info()

emp_2 = Employee()
emp_2.add_info("sara",800,"SR")
emp_2.print_info()

emp_3 = Employee()
emp_3.add_info("ahmed",500,"EGP")
emp_3.print_info()