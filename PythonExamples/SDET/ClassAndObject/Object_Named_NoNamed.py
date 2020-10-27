# Creating multiple objects of one class
class Student:
    """Creating multiple objects of one class"""

    def display(self, name):
        print(f"Hi {name}, Good morning")


obj1 = Student()  # Named object, Object has reference variable
obj1.display('Venkata')

Student().display('Babu')  # Named less object, Object has no reference variable
