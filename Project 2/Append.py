import csv

prefix = "https://www.fire.ca.gov"

with open('LinksOf2015.csv', 'r') as infile, open('done.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        row.insert(0,prefix)

        writer.writerow(row)
