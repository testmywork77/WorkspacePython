# __del__(self) method, to delete/destory the object
class MyClass:
    def __del__(self):
        print('Object destoryed')


obj1 = MyClass()
obj2 = MyClass()

print(obj1)
print(obj2)

del obj1
print(obj2)
print(obj1)

