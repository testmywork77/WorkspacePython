# Read .txt file with try.. except.. finally..
try:
    f = open("Demo1.txt")
    data = f.read()
    print(data)
except Exception as err:
    print("Exception is ", err)
finally:
    f.close()
