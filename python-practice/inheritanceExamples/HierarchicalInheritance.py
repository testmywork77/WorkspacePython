# Hierarchical Level Inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print("Method 1 in Class A ", self.x + self.y)
        

class B(A):
    a, b = 25, 35

    def m2(self):
        print("Method 2 in Class B ", self.a + self.b)


class C(A):
    i, j = 50, 40

    def m3(self):
        print("Method 3 in Class C ", self.i + self.j)


objA = A()
objA.m1()
print("-------------------")
objB = B()
objB.m2()
objB.m1()
print("-------------------")
objC = C()
objC.m3()
objC.m1()
