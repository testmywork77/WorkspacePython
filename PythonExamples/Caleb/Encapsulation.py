class Customer:
    # Overrided methods
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return self.name + " " + self.membership_type

    __hash__ = None

    __repr__ = __str__

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self, name):
        print("Setting name")
        self._name = name


customers = [Customer("Sam", "Gold"),
             Customer("Ram", "Bronze")]

print(customers)
