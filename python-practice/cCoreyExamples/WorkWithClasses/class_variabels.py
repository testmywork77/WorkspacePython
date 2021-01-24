# Python Object-Oriented Programming: Class Variables
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
        #return f"{self.fname} {self.lname}"
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Venkat', 'Mannepalli', 2000)
emp_2 = Employee('Abhi', 'Mannepalli', 4000)

print(f"No of employees: {Employee.num_of_emps}")
print("Full Name: {}".format(emp_1.fullname()))
print(f"Full Name: {emp_1.fullname()}")

'''
print(f"Employee: {Employee.raise_amount}")
print(f"emp1: {emp_1.raise_amount}")
print(f"emp2: {emp_2.raise_amount}")
emp_1.apply_raise()
emp_2.apply_raise()
print(f"Emp1: Pay before raise: {emp_1.pay}")
print(f"Emp2: Pay before raise: {emp_2.pay}")
'''

'''
#Employee.raise_amount = 3
#emp_1.raise_amount = 3
emp_2.raise_amount = 3
print(f"Employee: {Employee.raise_amount}")
print(f"emp1: {emp_1.raise_amount}")
print(f"emp2: {emp_2.raise_amount}")
emp_1.apply_raise()
emp_2.apply_raise()
print(f"Emp1: Pay after raise: {emp_1.pay}")
print(f"Emp2: Pay after raise: {emp_2.pay}")

# print(Employee.__dict__)
# print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
'''