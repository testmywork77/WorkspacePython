# __str__() method, by default will invoke when print reference variable i.e. Object
class MyClass:
    def func(self):
        print("__str__ example")


obj = MyClass()
obj.func()
print(obj)