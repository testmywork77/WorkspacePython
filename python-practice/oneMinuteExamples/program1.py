# Ask For A Number Input In Python

def asknum():
    while True:
        try:
            number = int(input("Number: "))
            print(f"You entered {number}")
            return number
        except ValueError:
            print("This is not a number")

asknum()
