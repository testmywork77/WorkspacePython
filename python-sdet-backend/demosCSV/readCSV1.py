import csv


with open('utilities/loanApp.csv') as readFile:
    csvReader = csv.reader(readFile, delimiter=',')
    print(list(csvReader))
    for row in csvReader:
        print(row)
