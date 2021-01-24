# Merge Two Dictionaries In Python

dict1 = {"k1": "v1", "k2": "v2"}
dict2 = {"k3": "v3", "k4": "v4"}

# Solution1: Unpack and create a new dict
dict3 = {**dict1, **dict2}
print(f"dict3: {dict3}")
# Contents of dict1 & dict2 doesn't change
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")

# Solution 2: Update contents of dict1 in place
dict1.update(dict2)
print("After update/merge dict2 into dict1: ")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
