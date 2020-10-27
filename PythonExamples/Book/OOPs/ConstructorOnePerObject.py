# Program to demonstrate constructor will execute only once per object
class Test:
    def __init__(self):
        print("Constructor execution")

    def m1(self):
        print("Method execution")


t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()
