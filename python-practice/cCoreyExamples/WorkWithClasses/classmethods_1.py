# Python Object-Oriented Programming: Class Methods_1
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        #return '{} {}'.format(self.fname, self.lname)
        return f"{self.fname} {self.lname}"        

    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Venkat', 'Mannepalli', 2000)
emp_2 = Employee('Abhi', 'Mannepalli', 4000)

print(f"No of employees: {Employee.num_of_emps}")
print(f"Employee: {Employee.raise_amount}")
print(f"emp1: {emp_1.raise_amount}")
print(f"emp2: {emp_2.raise_amount}")
Employee.set_raise_amount(1.05)
print(f"Employee: {Employee.raise_amount}")
print(f"emp1: {emp_1.raise_amount}")
print(f"emp2: {emp_2.raise_amount}")