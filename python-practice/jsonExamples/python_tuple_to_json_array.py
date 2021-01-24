# Python Tuple to JSON Array
import json

# Python tuple
tuple_example = 'Mango', 'Banana', 'Apple'
print(f"tuple_example data type : {type(tuple_example)}")  # tuple

# encoding JSON is called Serialization
to_json = json.dumps(tuple_example)

print(f"tuple_example data type: {type(to_json)}")  # str
print(to_json)

