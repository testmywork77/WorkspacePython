# Super()- To invoke parent class methods

class A:
    def m1(self):
        print("This method from Class A")


class B(A):
    def m2(self):
        print("This method from Class B")
        super().m1()  # Calling parent class method using super()


objB = B()
objB.m2()
