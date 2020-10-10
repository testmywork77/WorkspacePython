# Create Student class
class Student:
    # Default constructor
    def __init__(self):        
        self.sno=1
        self.sname="Abhinav"        
        self.age=13
        self.loc="Aylesbury"
        self.subjects=["Computers", "Maths", "Physics", "Chemistry"]

    # Print Student details
    def print_details(self):
        print(f"No: {self.sno}")
        print(f"Name: {self.sname}")
        print(f"Age: {self.age}")
        print(f"Location: {self.loc}")
        print(f"Subjects: {self.subjects}")    

# Create Object
student = Student()
student.print_details()