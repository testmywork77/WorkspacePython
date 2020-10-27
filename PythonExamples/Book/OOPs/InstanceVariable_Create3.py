# Outside of the class by using object reference variable

class Employee:
    """ Declare Instance variable- Outside of the class by using object reference variable """

    def __init__(self):
        self.eno = 1

    def method1(self):
        self.ename = 'Employee_1'


e = Employee()
e.method1()
e.esal = 2500
print(e.__doc__)
print(e.__dict__)
