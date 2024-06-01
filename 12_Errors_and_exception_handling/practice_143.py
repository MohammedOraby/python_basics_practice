# syntax error --> stop execute all code -- happens when check the roles off code
# Execution/Runtime errors (Exceptions) happens after check the role off code written and stops the execution only in error


print("program to divide two numbers")
x = int(input("enter first number : "))
y = int(input("enter second number : "))

try:
    print(x/y)
except ZeroDivisionError:
    print("cannot divide by zero")