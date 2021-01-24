class Student:
    """Class With Parameterized Constructor"""
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} Details:")
        print(f"Hello I am, {self.name}")
        print(f"My Number is, {self.rollno}")
        print(f"My Marks are, {self.marks}")


s1 = Student(1, 'Student_1', 75)
s1.display()

s2 = Student(2, 'Student_2', 80)
s2.display()
