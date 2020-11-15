# Converting JSON to Python Object(s)-dict, list, tuple
import json

my_json_string = """{
   "article": [

      {
         "id":"01",
         "language": "JSON",
         "edition": "first",
         "author": "Derrick Mwiti"
      },

      {
         "id":"02",
         "language": "Python",
         "edition": "second",
         "author": "Derrick Mwiti"
      }
   ],

   "blog":[
   {
       "name": "Datacamp",
       "URL":"datacamp.com"
   }
   ]
}
"""

# decoding JSON is called deserialization.
to_python = json.loads(my_json_string)

print(f"to_python's data type: {type(to_python)}")  # dict
print(to_python)
print(to_python['blog'])
