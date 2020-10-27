# Declare variables inside the class
# Class variables referred using self keyword
class MyClass:
    """Declare variables inside the class"""
    a, b = 10, 20  # Class variables

    def add(self):
        print(f"Sum is: {self.a + self.b}")  # Class variables referred in instance method with "self" keyword

    def mul(self):
        print(f"Product is: {self.a * self.b}")  # Class variables referred in instance method with "self" keyword


obj = MyClass()
print(obj.__doc__)
obj.add()
obj.mul()
