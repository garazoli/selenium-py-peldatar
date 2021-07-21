import csv

with open('table_in.csv') as table_in:
    csvreader = csv.reader(table_in, delimiter=',')
    for row in csvreader:
        with open('email_nev.csv', 'a') as file:
            file.write(row[1] + ',')
            file.write(row[0] + '\n')
