# Instance method and Static method
class MyClass:
    """Instance method and Static method"""

    # By default all the methods in class are Instance methods.Self is the default and must be first parameter
    def m1(self):
        print("Instance Method")

    @staticmethod
    def m2():
        print("Static Method")

    @staticmethod
    def m3(name):
        print(f"Name is: {name}")


obj = MyClass()
obj.m1()    # Instance method invoked by Object
MyClass.m2()  # Static methods invoked by Class
MyClass.m3('Venkata')
