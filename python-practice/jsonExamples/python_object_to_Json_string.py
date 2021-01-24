# Converting Python Objects to JSON
import json

blog = {'URL': 'datacamp.com', 'name': 'Datacamp'}

# encoding JSON is called Serialization
to_json = json.dumps(blog)

print(f"to_json data type: {type(to_json)}")  # str
print(to_json)
