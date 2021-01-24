# Constructor with arguments
class MyClass:
    """Constructor with arguments"""
    name = "XYZ"

    def __init__(self, name):
        print(name)  # local variable
        print(self.name)  # class variable


obj = MyClass('ABC')
print(obj.__doc__)
