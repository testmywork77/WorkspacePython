import json


# Parse content from .json file to Dict/List/Tuple
with open("course.json") as f:
    dict_course = json.load(f)
    print(dict_course)
    """
    print(type(dict_course))
    print(dict_course['courses'][1])
    print(dict_course['courses'][1]['title'])  # Get the title
    print(type(dict_course['dashboard']['website']))
    print(dict_course['dashboard']['website'])
    """
    # Get price of course "Selenium"
    for course in dict_course['courses']:
        # print(course)
        if course['title'] == "Selenium":
            print(course['price'])
            assert course['price'] == 45




