# Python Tuple to JSON Array
import json

# Python tuple
list_example = ['Mango', 'Banana', 'Apple']
print(f"list_example data type : {type(list_example)}")

# encoding JSON is called Serialization
to_json = json.dumps(list_example)

print(f"tuple_example data type: {type(to_json)}")  # str
print(to_json)

