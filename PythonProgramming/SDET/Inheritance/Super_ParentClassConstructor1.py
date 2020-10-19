# Super()- To invoke parent class constructor
class A:
    def __init__(self):
        print("Constructor from Class A")


class B(A):
    pass


objB = B()
