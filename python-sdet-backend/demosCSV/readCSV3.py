import csv


with open('utilities/loanApp.csv') as readFile:
    csvReader = csv.reader(readFile, delimiter=',')
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

# Retrieve Sam's loan status
index = names.index("Sam")
loanStatus = stats[index]
print(f"Sam's Loan Status: {loanStatus}")
