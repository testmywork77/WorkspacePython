import csv


with open('utilities/loanApp.csv') as readFile:
    csvReader = csv.reader(readFile, delimiter=',')
    for row in csvReader:
        print(row)
