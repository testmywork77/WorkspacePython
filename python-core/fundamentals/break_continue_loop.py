# break: Exits the loop.
"""
‌In the break example, the loop stops when i is equal to 3, and the numbers 0, 1, and 2 are printed.
"""
print("Loop control Break-range:")
for i in range(5):
    if i == 3:
        print(f"Encountered 'break' at i={i}") 
        break
    print(i)


print("Loop Control: Break")
temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

# continue: Skips the rest of the code inside the loop for the current iteration, then continues the loop.   
"""
In the continue example, when i is equal to 2, the continue statement skips the print(i) statement for that iteration, resulting in the omission of the number 2 from the output.
"""
print("Loop Control Continue -range:")
for i in range(5):
    if i == 2:
        print(f"Skipped iteration with 'continue' at i={i}")
        continue
    print(i)

print("Loop Control: Continue:")
for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))