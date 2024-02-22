# keyword Arguments
def user_info_kwargs(name, age=20, city="Bristol"):
    print(f'{name} is {age} years old, from {city}')

user_info_kwargs("Sam", 25, "London")
user_info_kwargs("Sam")

user_info_kwargs(city="Oxford", name="Ram", age=23)