class Student:
    """ Empty Constructor """

    def __init__(self):
        self.no = 1
        self.name = 'Student_1'
        self.marks = 50

    def display(self):
        print(f"Hello I am : {self.name}")
        print(f"My Number is: {self.no}")
        print(f"My Marks are: ", self.marks)


s = Student()
s.display()

