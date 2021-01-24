# Python Object-Oriented Programming: Classes and Instances
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return f"{self.fname} {self.lname}"

emp_1 = Employee('Venkat', 'Mannepalli', 2000)
emp_2 = Employee('Abhi', 'Mannepalli', 4000)

print(emp_1.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))

# print(emp_2.email)
# print(emp_2.fullname())