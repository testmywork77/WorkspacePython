# for loop Example 
"""
 A for loop is used when you know the number of iterations in advance.
"""
fruits = ["apple", "banana", "cherry"]
print("for loop:")
for fruit in fruits:
    print(fruit)


print("for loop with range:")
for number in range(1,5):
    print("Number {}".format(number))

# While Loop Example 
"""
A while statement is a control flow statement that allows you to execute a block of code repeatedly as long as a specified condition is true.  
"""
count = 0
print("while loop count:")
while count < 5:
    print("Count:", count)
    count += 1

print("while loop temp_f:")
temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1