# Inside Instance Method by using self variable
class Employee:
    """ Declare Instance variable- Inside Method by using self variable """

    def __init__(self):
        self.eno = 1
        self.ename = 'Employee_1'
        self.esal = 2500

    def method1(self):
        self.esal = 2500


e = Employee()
e.method1()
print(e.__dict__)
