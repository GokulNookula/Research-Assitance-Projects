import csv
import time
from functools import partial
from geopy.geocoders import Nominatim

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="ok",timeout= 2)

def isInsideCalifornia(lat, lon):
    # Define the polygon vertices (in the order they appear in my previous answer)
    vertices = [
    (42.0075, -124.2817),
    (41.9983, -120.0029),
    (35.0019, -114.0475),
    (33.0011, -114.7251),
    (32.5288, -117.2045),
    (33.6960, -118.5965)
    ]
    
    # Start with a point outside the polygon
    inside = False
    
    # Loop through each edge of the polygon
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        
        # Check if the ray intersects with this edge
        if ((vertices[i][1] > lon) != (vertices[j][1] > lon) and
            (lat < (vertices[j][0] - vertices[i][0]) * (lon - vertices[i][1]) / (vertices[j][1] - vertices[i][1]) + vertices[i][0])):
            inside = not inside
    
    return inside

# Load the CSV file with the coordinates
with open('modis_2004_United_States_2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)
    
    with open('United_States_2004_2.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Latitude","Longitude","Brightness","Scan","Track","Acq_Date","Acq_Time","Satellite","Instrument","Confidence","Version","Bright_t31","frp","daynight","givenType","County","Address"])

        # Loop through each row in the CSV file
        for row in csvreader:
            # Extract the latitude and longitude coordinates
            latitude = float(row[0])
            longitude = float(row[1])
            brightness = row[2]
            scan = row[3]
            track = row[4]
            acq_date = row[5]
            acq_time = row[6]
            satellite = row[7]
            instrument = row[8]
            confidence = row[9]
            version = row[10]
            bright_t31 = row[11]
            frp = row[12]
            daynight = row[13]
            givenType = row[14]

            # Check whether the coordinates are inside California's borders
            if isInsideCalifornia(latitude, longitude):
                print(f"{latitude}, {longitude}, {brightness}, {scan}, {track}, {acq_date}, {acq_time}, {satellite}, {instrument}, {confidence}, {version}, {bright_t31}, {frp}, {daynight}, {givenType} ")
                time.sleep(0.5)
                result = geolocator.reverse(f"{latitude}, {longitude}", addressdetails=True)
            
                county = result.raw['address'].get('county', '')
                address = result.address.replace(county, "").strip()

                # Write the row to the output file
                writer.writerow(row + [county, address])
