# Local, Class and Global variables with same name
# Local- Inside the method (l1,2)
# Class- Inside the class (C1, c2)
# Global- Outside the class (G1, G2)

a, b = 10, 20  # Global


class MyClass:
    """Local, Class and Global variables with same name"""
    a, b = 30, 40  # Class

    def method(self, a, b):  # Local
        print(f"Local: {a+b}")  # Access Local variables
        print(f"Class: {self.a + self.b}")  # Access Class variables
        print(f"Global: {globals() ['a'] + globals() ['b']}")  # Access Global variables


obj = MyClass()
print(obj.__doc__)
obj.method(50, 25)
