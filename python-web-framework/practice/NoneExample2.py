import re


match = re.match(r"Hello", "Hello World!")
# Do use the identity operators is and is not.
if match is None:
    print(type(match))
    print("It doesn't match.")
else:
    print(type(match))
    print("It's match")
