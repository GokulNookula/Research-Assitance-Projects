import csv

# Open the input and output files
with open('United_States_2021.csv', 'r') as infile, open('done.csv', 'w', newline='') as outfile:
    # Create a CSV reader and writer
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row to the output file (if applicable)
    header = next(reader, None)
    if header is not None:
        writer.writerow(header)

    # Iterate through each row of the input file
    for row in reader:
        # Check if the last column contains "CAL Fire San Diego Unit"
        if "CAL Fire San Diego Unit" in row[-1]:
            # Add the county name to the output
            row.insert(-2, "San Diego County")
        elif "CAL Fire Kern County" in row[-1]:
            row.insert(-2,"Kern County")
        elif "CAL Fire Lassen Modoc Plumas Unit" in row[-1]:
            row.insert(-2,"Lassen County")
        elif "CAL Fire San Bernardino Unit" in row[-1]:
            row.insert(-2,"San Bernardino County")
        # Write the modified row to the output file
        writer.writerow(row)

print("Done :D")
