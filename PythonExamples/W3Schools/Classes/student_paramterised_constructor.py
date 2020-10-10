# Create Student class
class Student:
    # Default constructor
    def __init__(self, no, name, age, location, subjects):        
        self.no=no
        self.name=name       
        self.age=age
        self.location=location
        self.subjects=subjects

    # Print Student details
    def print_details(self):
        print(f"No: {self.no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Subjects: {self.subjects}")  
        print("***============================================***")  

# Create Object
no = 1
name = "Abhinav"
age = 13
location = "Aylesbury"
subjects = ["Computers", "Maths", "Physics", "Chemistry"]
# abhinav = Student(1, "Abhinav", 13, "Aylesbury", ["Computers", "Maths", "Physics", "Chemistry"])
abhinav = Student(no, name, age, location, subjects)
abhinav.print_details()

'''
lucas = Student(2, "Lucas", 13, "Aylesbury", ["Computers", "Maths", "Physics", "Chemistry"])
lucas.print_details()
'''