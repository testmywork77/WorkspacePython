# Python Object-Oriented Programming: Static Methods
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

    @staticmethod
    def is_workday(day):    
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True   

import datetime
#my_date = datetime.date(2020, 8, 22)
my_date = datetime.datetime.now()
print(f"Is Today is working day? {Employee.is_workday(my_date)}")