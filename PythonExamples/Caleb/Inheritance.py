class User:
    def log(self):
        print(self)


class Customer(User):
    # Overrided methods
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return self.name + " " + self.membership_type

    __repr__ = __str__


customers = [Customer("Sam", "Gold"),
             Customer("Ram", "Bronze")]

print(customers)
customers[0].log()
