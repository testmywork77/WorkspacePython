# Convert local variables into class variables
class MyClass:
    """Convert local variables into class variables"""
    def method1(self, val1, val2):  # local variables
        print(val1)
        print(val2)
        self.val1 = val1
        self.val2 = val2

    def method2(self):
        print(self.val1+self.val2)


obj = MyClass()
obj.method1(4, 6)
obj.method2()
