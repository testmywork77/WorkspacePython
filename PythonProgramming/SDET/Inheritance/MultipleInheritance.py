# Multiple Inheritance
class A:
    def m1(self):
        print("Method 1 in Class A")


class B():
    def m2(self):
        print("Method 2 in Class B")


class C(A, B):
    def m3(self):
        print("Method 3 in Class C")


objA = A()
objA.m1()
print("-------------------")
objB = B()
objB.m2()
print("-------------------")
objC = C()
objC.m3()
objC.m2()
objC.m1()
