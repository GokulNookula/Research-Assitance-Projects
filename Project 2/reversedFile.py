import csv

with open('LinksOf2015.csv', 'r') as infile, open('done.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read rows into a list, reverse the order, and write to output file
    rows = list(reversed(list(reader)))
    writer.writerows(rows)
