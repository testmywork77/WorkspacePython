# Super()- To invoke parent class variables with different name

class A:
    a, b = 10, 20

    def m1(self):
        print("This method from Class A")


class B(A):
    i, j = 30, 40

    def m2(self, x, y):
        print(f"Local sum of x and y: {x+y}")  # Local variables
        print(f"Class sum of i and j: {self.i + self.j}")  # Child class variables
        print(f"Parent Class sum of a and b: {self.a + self.b}")  # Parent class variables


objB = B()
objB.m2(40, 50)
