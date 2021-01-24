# Read A CSV File In Python
import csv

with open('employee.csv') as f:
    for row in csv.DictReader(f):
        print(f"{row['eno']} {row['ename']} {row['loc']}")

