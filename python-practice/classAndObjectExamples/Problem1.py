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

    def display(self):
        print(f"EId is: {self.eid}, Ename is: {self.ename} and Salary is: {self.esal}")
        print("EId is: {}, Ename is: {} and Salary is: {}".format(self.eid, self.ename, self.esal))
        print("EId is: %d, Ename is: %s and Salary is: %d" %(self.eid, self.ename, self.esal))


obj = Emp(1, 'ename1', 2500.25)
obj.display()
