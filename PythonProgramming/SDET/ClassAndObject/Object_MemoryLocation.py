# How to check memory locations of objects?
class MyClass:
    """How to check memory locations of objects?"""
    def func(self):
        pass


obj1 = MyClass()
obj2 = MyClass()
obj3 = obj1

print(f"Address of obj1: {id(obj1)}")
print(f"Address of obj2: {id(obj2)}")
print(f"Address of obj3: {id(obj3)}")

print(obj1 is obj2)  # False
print(obj1 is obj3)  # True

print(obj1 is not obj2)  # True
print(obj1 is not obj3)  # False

