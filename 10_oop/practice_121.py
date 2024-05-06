class Employee:
    def print_info(elf):
        print(f"name : {elf.name} , salary : {elf.salary}{elf.currency}")

emp_1 = Employee()
emp_2 = Employee()

emp_1.name = "mohamed"
emp_1.salary = 500
emp_1.currency = "$"

emp_2.name = "sara"
emp_2.salary = 700
emp_2.currency = "SR"

emp_3 = Employee()
emp_3.name = "ali"
emp_3.salary = 900
emp_3.currency = "YEN"

emp_1.print_info()
emp_2.print_info()
emp_3.print_info()
