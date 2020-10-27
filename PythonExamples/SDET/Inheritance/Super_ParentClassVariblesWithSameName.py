# Super()- To invoke parent class variables with same name
a, b = 10, 15

class A:
    a, b = 10, 20

    def m1(self):
        print("This method from Class A")


class B(A):
    a, b= 30, 40

    def m2(self, a, b):
        print(f"Local variables sum of x and y: {a+ b}")  # Local variables
        print(f"Class variables sum of i and j: {self.a + self.b}")  # Child class variables
        print(f"Parent Class variables sum of a and b: {super().a + super().b}")  # Parent class variables
        print(f"Global variables sum of a and b: {globals() ['a'] + globals() ['b']}")  # Global variables


objB = B()
objB.m2(40, 50)
