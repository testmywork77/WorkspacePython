# __init__ -is a Initializer/ Constructor,
# self, means current instance i.e. this in java/javascript
# __str__, override the .toString() functionality of the current instance/object
# __eq__, override the comparison of two objects
class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return self.name + " " + self.membership_type

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    def update_membership(self, new_membership_type):
        # invoke an API / update a database / charge the customer / calculate costs
        self.membership_type = new_membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)


customers = [Customer("Sam", "Gold"),
             Customer("Ram", "Bronze")]

print("Customer Objects Address: {}, {}".format(id(customers[0]), id(customers[1])))
print("Compare two different objects address & content")
# if we don't override __eq__, by default it compares with address instead of content
print(id(customers[0]) == id(customers[1]))
print(customers[0] == customers[1])
customers.clear()
customers = [Customer("Sam", "Gold"),
             Customer("Sam", "Gold")]
print("Compare two same objects address & content")
# if we don't override __eq__, by default it compares with address instead of content
print(id(customers[0]) == id(customers[1]))
print(customers[0] == customers[1])
