# Read .txt file
f = open("Demo.txt")
data = f.read()
print(f.name)
print(f.mode)
print(data)
print(f"Before file close: {f.closed}")
f.close()
print(f"After file close: {f.closed}")

