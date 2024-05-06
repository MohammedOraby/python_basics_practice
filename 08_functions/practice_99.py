## Loop variables are not block-scoped in python

x = "ahmed"

def f():
    for x in range(5):
        print("HI")
f()
print(f"after function value of x: {x}")

for x in range(5):
    print("hello")

print(f"after loop value of x: {x}")