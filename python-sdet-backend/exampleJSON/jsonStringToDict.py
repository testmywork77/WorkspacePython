import json

#  A multiline string in Python begins and ends with either three single quotes or three double quotes.
courses = '''
    {
    "name": "Name1",    
    "languages": [
        "Java",
        "C#"
    ]
}
'''

# Loads method parse the json string and returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
print(dict_courses['languages'][0])
"""
list_languages = dict_courses['languages']
print(type(list_languages))
print(list_languages[0])
"""
