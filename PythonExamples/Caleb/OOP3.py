# __init__ -is a Initializer/ Constructor,
# self, means current instance i.e. this in java/javascript
# __str__, override the .toString() functionality of the current instance/object
class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return self.name + " " + self.membership_type

    def update_membership(self, new_membership_type):
        # invoke an API / update a database / charge the customer / calculate costs
        self.membership_type = new_membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)


customers = [Customer("Sam", "Gold"),
             Customer("Ram", "Bronze")]

Customer.print_all_customers(customers)
