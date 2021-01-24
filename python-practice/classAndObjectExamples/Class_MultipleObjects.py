# Creating multiple objects of one class
class Student:
    """Creating multiple objects of one class"""

    def display(self, name):
        print(f"Hi {name}, Good morning")


obj1 = Student()
obj1.display('Venkata')

obj2 = Student()
obj2.display('Babu')
