# *args -allows a function to take any number of positional arguments.
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(2, 3))
print(add(2, 3, 4))
print(add(2, 3, 4, 5))

# **kwargs -allows a function to take any / variable number of keyword arguments to a function
def user_info(**kwargs):
    print(kwargs)

user_info(id=1)
user_info(id=1, name="Scott")
user_info(id=1, name="Scott")
user_info(id=1, name="Scott", city="London")
user_info(id=1, name="Scott", city="London", email="Scott@gmail1.com")