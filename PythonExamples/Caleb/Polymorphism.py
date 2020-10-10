class User:
    def log(self):
        print(self)


class Teacher(User):
    def log(self):
        print("I'm a teacher!")


class Customer(User):
    def log(self):
        print("I'm a customer!")

    # Overrided methods
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def __str__(self):
        return self.name + " " + self.membership_type

    __repr__ = __str__


users = [Customer("Sam", "Gold"),
         Customer("Ram", "Bronze"),
         Teacher()]

for user in users:
    user.log()
