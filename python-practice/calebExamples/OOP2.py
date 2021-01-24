# __init__ -is a Initializer/ Constructor,
# self -, __str__
class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership_type):
        # invoke an API / update a database / charge the customer / calculate costs
        self.membership_type = new_membership_type

    def __str__(self):
        return self.name + " " + self.membership_type


customers = [Customer("Sam", "Gold"),
             Customer("Ram", "Bronze")]

print(customers[0])

print(customers[1])
customers[1].update_membership("Silver")
print(customers[1])
