## scope: local scope and global scope

def f1():
    x = 10
    print(x)
x = 99

def f2():
    x = 11
    print(x)

f1()
f2()
print(x)