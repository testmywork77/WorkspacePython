# Python Object-Oriented Programming: Getter, Setter and Deleter
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return f"{self.fname} {self.lname}"

emp_1 = Employee('Venkat', 'Mannepalli', 2000)

print(emp_1.fname)
print(emp_1.lname)
print(emp_1.email)
print(emp_1.fullname())