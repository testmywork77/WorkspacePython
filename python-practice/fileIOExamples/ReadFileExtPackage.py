# Read external file, which is in other package with Context Manager
import os

cwd = os.getcwd()  # cwd - current working directory
print(cwd)
print(os.path.dirname(cwd))

with open(os.path.dirname(cwd) + "\\General\\Hello.txt") as f:
    print(f"Current state is: {f.closed} ")
    data = f.read()
    print(data)

print(f"State of the file is: {f.closed}")
