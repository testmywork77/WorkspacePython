# Constructor
class MyClass:
    """Constructor"""
    def display(self):
        print("Good morning")

    def __init__(self):
        print("Constructor executed")


obj = MyClass()
obj.display()
