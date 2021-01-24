# Local, Class and Global variables
# Local- Inside the method (l1,2)
# Class- Inside the class (C1, c2)
# Global- Outside the class (G1, G2)

g1, g2 = 10, 20  # Global


class MyClass:
    c1, c2 = 30, 40  # class

    def method(self, l1, l2):  # Local
        print(f"Local: {l1+l2}")  # Access Local variables
        print(f"Class: {self.c1 + self.c2}")  # Access Class variables
        print(f"Global: {g1 + g2}")  # Access Global variables


obj = MyClass()
obj.method(50, 25)
