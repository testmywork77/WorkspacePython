class Employee:
    ### A sample employee class ###

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

    @property
    def name(self):
        return f"{self.fname} {self.lname}"