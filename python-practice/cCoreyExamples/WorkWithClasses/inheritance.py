# Python Object-Oriented Programming: Inheritance

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

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay )
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)            

    def print_emps(self):
        for emp in self.employees:
            print(f"Name: {emp.fullname()}")

dev_1 = Developer('Venkat', 'Mannepalli', 2000, 'Python')
dev_2 = Developer('Abhi', 'Mannepalli', 4000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 5000, [dev_1])

'''
print("***Employee details***")
mgr_1.print_emps()

mgr_1.add_emp(dev_2)
print("***Employee details after add***")
mgr_1.print_emps()

mgr_1.del_emp(dev_1)
print("***Employee details after delete***")
mgr_1.print_emps()
'''
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Developer))

#print(help(Developer))
#print(dev_1.__dict__)
#print(dev_2.__dict__) 