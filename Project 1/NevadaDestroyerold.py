import csv

# Define the list of filters
filters = [', Nevada, United States', ', Nevada, 89448, United States', ', Nevada, 89111, United States',
           ', Nevada, 89406, United States', ', Nevada, 89413, United States', ", Nevada, 89521, United States",
           ", Nevada, 89449, United States",", Nevada, 89560, United States",", Nevada, 89523, United States",
           ", Nevada, 89410, United States",", Nevada, 89444, United States",", Nevada, 89508, United States",
           ", Nevada, 89447, United States",", Nevada, 89519, United States",", Nevada, 89509, United States",
           ", Nevada, 89511, United States",", Nevada, 89431, United States",", Nevada, 89020, United States",
           ", Nevada, 89703, United States",", Nevada, 89515, United States",", Nevada, 89439, United States",
           ", Nevada, 89011, United States",", Nevada, 89451, United States",", Nevada, 89408, United States",
           ", Nevada, 89427, United States",", Nevada, 89506, United States",", Nevada, 89060, United States",
           ", Nevada, 89004, United States",", Nevada, 89110, United States",", Nevada, 89701, United States",
           ", Nevada, 89450, United States",", Nevada, 89061, United States",", Nevada, 89504, United States",
           ", Nevada, 89434, United States",", Nevada, 89029, United States",", Nevada, 89496, United States",
           ", Nevada, 89403, United States",", Nevada, 89341, United States",", Nevada, 89428, United States",
           ", Nevada, 89161, United States",", Nevada, 89419, United States",", Nevada, 89702, United States",
           ", Nevada, 89460, United States",", Nevada, 89704, United States",", Nevada, 89430, United States",
           ", Nevada, 89411, United States",", Nevada, 89407, United States",", Nevada, 89433, United States",
           ", Nevada, 89124, United States",", Nevada, 89412, United States",", Nevada, 89022, United States",
           ", Nevada, 89115, United States",", Nevada, 89705, United States",", Nevada, 89014, United States",
           ", Nevada, 89028, United States",", Nevada, 89112, United States",", Nevada, 89019, United States"]

# Open the input and output CSV files
with open('InputFile.csv', 'r') as infile, open('OutputFile.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header row to the output file (if applicable)
    header = next(reader, None)
    if header is not None:
        writer.writerow(header)
    
    # Write all the rows that don't match any filter to the output file
    for row in reader:
        if not any(row[-1].endswith(filter_str) for filter_str in filters):
            writer.writerow(row)

print("Done")
