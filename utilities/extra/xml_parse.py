import csv

def parseTable(csv_file):
    with open(csv_file, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)

parseTable('comparison.csv')

