class MyClass:
    x = 20

    def __init__(self,param_1,param_2):
        self.attr_1 = param_1
        self.attr_2 = param_2

    def method_1(self):
        MyClass.x = 90

obj_1 = MyClass(10,11)
obj_2 = MyClass(12,13)

print(obj_1.x,obj_2.x)
obj_1.method_1()
print(obj_1.x,obj_2.x)




# obj_2.x = 21
# print(obj_2.x)

# MyClass.x = 70
# print(MyClass.x)
# print(obj_1.x)
# print(obj_2.x)

# print(obj_1.attr_1,obj_1.attr_2)
# obj_2.attr_1 = 9
# print(obj_2.attr_1,obj_2.attr_2)


