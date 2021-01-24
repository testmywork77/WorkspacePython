# Super()- To invoke parent class constructor
class A:
    def __init__(self):  # Parent class constructor
        print("Constructor from Class A")


class B(A):
    def __init__(self):  # Child class constructor
        print("Constructor from Class B")
        super().__init__()  # Approach1- Calls Parent class constructor
        A.__init__(self)  # Approach2- Calls Parent class constructor


objB = B()
