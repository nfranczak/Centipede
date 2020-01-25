import csv
import operator
import os

with open('liz copy.csv', 'r') as csv_file:
    with open('new liz copy.csv', 'w') as manipulated_csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')

        sort = sorted(csv_reader, key = lambda row: int(row[1]))
        writer = csv.writer(manipulated_csv_file)

        for row in sort:
            if ' Header' in row:
                writer.writerow(row)
            elif ' Time_signature' in row:
                writer.writerow(row)
            elif ' Key_signature' in row:
                writer.writerow(row)
            elif ' Marker_t' in row:
                writer.writerow(row)
            elif ' Tempo' in row:
                writer.writerow(row)
            elif ' Note_on_c' in row:
                writer.writerow(row)
            else:
                pass

with open('new liz copy.csv', 'r') as manipulated_csv_file:
    for row in manipulated_csv_file:
        print row
