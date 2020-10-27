# How to call current class method in another method
class MyClass:
    def m1(self):
        print("In M1 method")
        self.m2(12)

    def m2(self, a):
        print("In M2 method", a)


obj = MyClass()
obj.m1()
