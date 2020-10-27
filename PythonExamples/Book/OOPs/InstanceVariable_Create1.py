# Inside Constructor by using self variable
class Employee:
    """ Declare Instance variable- Inside Constructor by using self variable """
    def __init__(self):
        self.eno = 1
        self.ename = 'Employee_1'
        self.esal = 2500

    # def display(self):
    #     print(f"Hello I am : {self.ename}")
    #     print(f"My Number is: {self.eno}")
    #     print(f"My Marks are: ", self.esal)


e = Employee()
print(e.__doc__)
print(e.__dict__)
