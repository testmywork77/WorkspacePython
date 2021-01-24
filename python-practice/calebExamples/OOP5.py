# __init__ -is a Initializer/ Constructor,
# self, means current instance i.e. this in java/javascript
# __str__, override the .toString() functionality of the current instance/object
# __repr__, equivalent to __str__, used for collections
class Customer:
    # Overrided methods
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return self.name + " " + self.membership_type

    __hash__ = None
    
    __repr__ = __str__


customers = [Customer("Sam", "Gold"),
             Customer("Ram", "Bronze")]

print(customers)
