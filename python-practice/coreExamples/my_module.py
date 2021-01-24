# What is if __name__ == "__main__" ??
"""
    Every module in Python has a special attribute called __name__. 
    The value of __name__  attribute is set to '__main__'  when module run as main program.
     Otherwise, the value of __name__  is set to contain the name of the module.
"""

foo = 100

def hello():
    print("i am from my_module.py")

if __name__ == "__main__":
    print("Executing as a main program")
    print(f"value of __name__ is: {__name__}")
    hello()