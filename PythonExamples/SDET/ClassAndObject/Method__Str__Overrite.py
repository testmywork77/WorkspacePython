"""
    Problem 1:
    Class Name: Emp
    Constructor: Accepts eid, ename, esal
    Display Method: print eid, ename, esal
"""


class Emp:
    def __init__(self, eid, ename, esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):  # __str__ overridden
        return f"EId is: {self.eid}, Ename is: {self.ename} and Salary is: {self.esal}"


obj = Emp(1, 'ename1', 2500.25)
print(obj)  # by default, __str__  method will be invoked and return value
