class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type


c1 = Customer("Venkata", "Gold")
print(c1.name, c1.membership_type)

c2 = Customer("Ram", "Bronze")
print(c2.name, c2.membership_type)
