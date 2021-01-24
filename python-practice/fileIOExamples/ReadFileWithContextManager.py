# Context Manager
with open("Demo.txt") as f:
    print(f"Current state is: {f.closed} ")
    data = f.read()
    print(data)

print(f"State of the file is: {f.closed}")
