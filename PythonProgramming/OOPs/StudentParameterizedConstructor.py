class Student:
    """Class With Parameterized Constructor"""
    def __init__(self, no, name, age):
        self.no = no
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hello I am : {self.name}")
        print(f"My Number is: {self.no}")
        print(f"My Marks are: ", self.marks)


s = Student(2, 'Student_2', 75)
s.talk()
