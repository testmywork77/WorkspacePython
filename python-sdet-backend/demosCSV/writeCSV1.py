import csv

# To append to existing .csv file
with open('utilities/loanApp.csv', 'a') as writeFile:
    csvWriter = csv.writer(writeFile)
    csvWriter.writerow(["Bob", "Approved"])

# To read file
with open('utilities/loanApp.csv') as readFile:
    csvReader = csv.reader(readFile, delimiter=',')
    for row in csvReader:
        print(row)
