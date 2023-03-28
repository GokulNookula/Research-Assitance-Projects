from bs4 import BeautifulSoup
import requests
import csv

#Insert the Url Link where you want to extract the stuff from
url = "https://www.fire.ca.gov/incidents/2022/2/16/airport-fire"

#Change the reference page when your trying to access different years from the above website or you will get Forbidden Acess aka <Response [403]
headers = {
    'User-Agent': '#Put your user agent by typing my user agent in the whaterver web browser your using',
    'Referer': '#give a reference here'
}

response = requests.get(url,headers=headers)

# To check response time if it is working or not
# print(response)

# use BeautifulSoup to parse the HTML
soup = BeautifulSoup(response.content,"html.parser")


NameOfTheFire = soup.find("h1").text.strip()
print(NameOfTheFire)

# Find the <li> tag that contains the acres information
acres = soup.find('li', string=lambda s: s and 'Acres' in s)

# Extract the acres information
acres_text = acres.string.strip().replace(',', '')
# Acres_Num contains my Acres that I need
acres_num = int(acres_text.split()[0])

# Print the acres information
print(acres_num)

county = soup.find('li', string=lambda s: s and 'County:' in s).string.strip().split(':')[-1].strip()
print(county)

crew_number = soup.find("div", class_="factoid__label", string="Crews").find_previous_sibling("div", class_="factoid__data").text.strip()
print(crew_number)

# Extract the relevant information
dateStarted = soup.find('strong', string='Last Updated').find_next('div').text.strip()
dateStarted = dateStarted[14:23]
dateContained = soup.find('strong', string='Date Started').find_next('div').text.strip()
dateContained = dateContained[16:25]
locationInformation = soup.find('strong', string='Date Contained').find_next('div').text.strip()
locationInformation = locationInformation[20:]
latitudeAndLongitude = soup.find('strong', string='Location Information').find_next('div').text.strip()
latitudeAndLongitude = latitudeAndLongitude[21:]
latitude, longitude = latitudeAndLongitude[1:-1].split(',')
cause = soup.find('strong', string='Admin Unit').find_next('div').text.strip()
cause = cause[6:]

# Print the extracted information
print(dateStarted) 
print(dateContained)
print(locationInformation)
print(latitude)
print(longitude)
print(cause)

# numStructuresDamaged = soup.find("div", class_="factoid__label", string="Structures Damaged").find_previous_sibling("div", class_="factoid__data").text.strip()
# print(numStructuresDamaged)


# numStructuresDestroyed = soup.find("div", class_="factoid__label", string="Structures Destroyed").find_previous_sibling("div", class_="factoid__data").text.strip()
# print(numStructuresDestroyed)

# fatality = soup.find("div", class_="factoid__label", string="Fatality").find_previous_sibling("div", class_="factoid__data").text.strip()
# print(fatality)

# injuries = soup.find("div", class_="factoid__label", string="Injuries").find_previous_sibling("div", class_="factoid__data").text.strip()
# print(injuries)

try:
    numStructuresDamaged = soup.find("div", class_="factoid__label", string="Structures Damaged").find_previous_sibling("div", class_="factoid__data").text.strip()
except AttributeError:
    numStructuresDamaged = None

try:
    numStructuresDestroyed = soup.find("div", class_="factoid__label", string="Structures Destroyed").find_previous_sibling("div", class_="factoid__data").text.strip()
except AttributeError:
    numStructuresDestroyed = None

try:
    fatality = soup.find("div", class_="factoid__label", string="Fatality").find_previous_sibling("div", class_="factoid__data").text.strip()
except AttributeError:
    fatality = None

try:
    injuries = soup.find("div", class_="factoid__label", string="Injuries").find_previous_sibling("div", class_="factoid__data").text.strip()
except AttributeError:
    injuries = None

print(numStructuresDamaged)
print(numStructuresDestroyed)
print(fatality)
print(injuries)





















# "Name of the Fire","County / Counties", "Date Started","Date Contained", "Acres", "Latitude", "Longitude", "Cause", "Location Information", "Crews (Number of Fire Fighter Crews)",
# "Number of Structures Damaged", "Number of Structures Destroyed", "Fatality, Injuries"

