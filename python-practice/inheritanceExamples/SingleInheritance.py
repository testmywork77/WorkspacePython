# Single Inheritance
class A:
    def m1(self):
        print("Method 1 in Class A")


class B(A):
    def m2(self):
        print("Method 2 in Class B")


objA = A()
objA.m1()

objB = B()
objB.m2()
objB.m1()
