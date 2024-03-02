# Conditional Statements (if, elif, else)
# docstrings -instead of having to put a hashtag in front of each line, if you can use this """ """ comment.
"""
The if statement checks if age is less than 18.
The elif statement (shorthand for else if) checks if age is between 18 (inclusive) and 21 (exclusive).
The else statement is executed if none of the above conditions are met.
"""
age = int(input("enter age: "))
if age < 18:
    print("You are a minor.")
elif 18 <= age < 21:
    print("You are an adult, but not yet allowed to drink.")
else:
    print("You are a legal adult.")