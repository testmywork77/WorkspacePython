# "New Style" String Formatting using str.format (Python 3)

name = "John"
school = "Turnfurlong School"
"""
The format method or format function actually accepts the arguments of our variables and transfers those arguments into the curly braces in the order that they appear in the sentence.
"""
print("srt.format: {0} works at {1}.".format(name, school))

# String Interpolation / f-Strings (Python 3.6+) 
# Most recommended after Python 3.6+
print(f'f-Strings: {name} works at {school}.')

def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

print(greet('Bob', 'going'))

# variables
quantity, item, price = 6, 'bananas', 1.74
f'{quantity} {item} cost ${price}'
 
# Arithmetic expressions:
x = 6
print(f'{x} cubed is {x**3}')

# Objects of composite types
a = ['foo', 'bar', 'baz']
d = {'foo': 1, 'bar': 2}
print(f'a = {a} | d = {d}') # a = ['foo', 'bar', 'baz'] | d = {'foo': 1, 'bar': 2}

# Indexing, slicing, and key references:
a = ['foo', 'bar', 'baz']
d = {'foo': 1, 'bar': 2}

print(f'First item in list a = {a[0]}')
print(f'Last two items in list a = {a[-2:]}')
print(f'List a reversed = {a[::-1]}')
print(f"Dict value for key 'bar' is {d['bar']}")

# Function and method calls
a = ['foo', 'bar', 'baz', 'qux', 'quux']
print(f'List a has {len(a)} items')


s = 'foobar'
print(f'--- {s.upper()} ---')


d = {'foo': 1, 'bar': 2}
print(f"Dict value for key 'bar' is {d.get('bar')}")


# Conditional expressions
x = 3
y = 7
print(f'The larger of {x} and {y} is {x if x > y else y}')

age = 13
f'I am {"a minor" if age < 18 else "an adult"}.'
