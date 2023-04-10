import csv

with open("test.csv",'r') as infile, open('done.csv','w',newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    writer.writerow(["Name of the Fire","County / Counties", "Date Started","Date Contained"
                , "Acres", "Latitude", "Longitude", "Cause", "Location Information", "Crews (Number of Fire Fighter Crews)"
                ,"Number of Structures Damaged", "Number of Structures Destroyed", "Fatality", "Injuries"])

    for row in reader:
        incident = row[0]
        contpercent = row[1]
        county = row[2]
        firename = row[3]
        startDate = row[4]
        containedDate = row[5]
        origin = row[6]
        acres = row[7]
        other = row[8]
        total = row[9]
        vegType = row[10]
        cause = row[11]
        struct_dest = row[12]
        struct_dam = row[13]
        fatalities_fire = row[14]
        fatalities_civil = row[15]
        latitude = ''
        longitude = ''
        locationInformation = ''
        crews = ''
        fataility = ''
        injuries = ''


        writer.writerow([firename,county,startDate,containedDate,acres,
                         latitude,longitude,cause,locationInformation,struct_dam,struct_dest,fataility,injuries])

