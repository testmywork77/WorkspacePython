import json


with open("course1.json") as f1:
    course1_dict = json.load(f1)
    print(f"Course1 JSON:\n {course1_dict}")

with open("course2.json") as f2:
    course2_dict = json.load(f2)
    print(f"Course2 JSON:\n {course2_dict}")

assert course1_dict == course2_dict
