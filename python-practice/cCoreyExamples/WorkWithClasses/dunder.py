# Python Object-Oriented Programming: Magic/Dunder methods

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

    def __repr__(self):
        #return "Employee('{}','{}',{})".format(self.fname, self.lname, self.pay)
        return f"Employee( '{self.fname}','{self.lname}',{self.pay})"

    def __str__(self):
        #return "{} - {}".format(self.fname)       
        return f"{self.fullname()}-{self.email}"

emp1_1 = Employee('Venkata', 'Mannepalli', 2000)
emp_2 = Employee('Abhi', 'Mannepalli', 4000)

print(emp1_1)
print(repr(emp1_1))
print(str(emp1_1))

print(emp1_1.__repr__())
print(emp1_1.__str__())