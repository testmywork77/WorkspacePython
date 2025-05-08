fruits = ["peaches", "pears",  "apples"]
years = [3, "1998", 2.5, 987, "1994"]
print(fruits)

print("List Method: Append")
fruits.append("oranges")
print(fruits)

print("List Method: Extend")
fruits.extend(years)
print(fruits)

print("List Method: Remove")
fruits.remove("oranges")
print(fruits)

print("List Method: Pop")
fruits.pop(0)
print(fruits)

print("List Method: Sort -can only be used with lists of like types.")
fruits = ["peaches", "pears",  "apples"]
print(fruits)
fruits.sort()
print(fruits)

print("Checking Membership in a List & count:")
fruits = ["peaches", "apples", "pears", "apples", "apples"]
print("apples" in fruits)
print(f'apples count: {fruits.count("apples")}')

print("check membership as well as the index position using the index function.")
print(f'index: {fruits.index("pears")}')




