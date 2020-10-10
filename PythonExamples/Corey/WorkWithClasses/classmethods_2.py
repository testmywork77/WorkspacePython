# Python Object-Oriented Programming: Class Methods_2
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

    # Alternative constructor for classes
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        cls(fname, lname, pay)

emp_str_1 = 'John-Doe-40000'
emp_str_2 = 'Steve-Smith-50000'
emp_str_3 = 'Ram-Lakshman-60000'

new_emp_1 = Employee.from_string(emp_str_1)

print(f"Full Name: {new_emp_1.fullname()}")
print(f"Email: {new_emp_1.email}")