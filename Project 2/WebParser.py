from bs4 import BeautifulSoup
import requests
import csv

#Insert the Url Link where you want to extract the stuff from
urls = ["#insert url here","#insert another url here"]

#Change the reference page when your trying to access different years from the above website or you will get Forbidden Acess aka <Response [403]
headers = {
    'User-Agent': '#Put your user agent by typing my user agent in the whaterver web browser your using',
    'Referer': '#give a reference here'
}

with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Name of the Fire","County / Counties", "Date Started","Date Contained"
                    , "Acres", "Latitude", "Longitude", "Cause", "Location Information", "Crews (Number of Fire Fighter Crews)"
                    ,"Number of Structures Damaged", "Number of Structures Destroyed", "Fatality", "Injuries"])

     for url in urls:

        response = requests.get(url,headers=headers)
        #To check if we can access the website or not
        # print(response)

        if (response.status_code == 200):

            # use BeautifulSoup to parse the HTML
            soup = BeautifulSoup(response.content,"html.parser")

            NameOfTheFire = soup.find("h1").text.strip()
            #Check if it works or not test case use the code below
            # print(NameOfTheFire)

            county_element = soup.find('li', string=lambda s: s and ('County:' in s or 'Counties:' in s))
            if county_element is not None:
                if 'County:' in county_element.string:
                    county = county_element.string.strip().split(':')[-1].strip()
                elif 'Counties:' in county_element.string:
                    county_list = [county.strip() for county in county_element.string.split(':')[1].split(',')]
                    county = ", ".join(county_list)
            else:
                county = None

            dateStarted = soup.find('strong', string='Last Updated').find_next('div').text.strip()
            dateStarted = dateStarted[13:23]
            #Check if it works or not test case use the code below
            # print(dateStarted) 

            dateContained = soup.find('strong', string='Date Started').find_next('div').text.strip()
            if "Date Contained" in dateContained:
                dateContained = dateContained[15:25]
                #Check if it works or not test case use the code below
                # print(dateContained)
            else:
                dateContained = None

            try:
                # Find the <li> tag that contains the acres information
                acres = soup.find('li', string=lambda s: s and 'Acres' in s)

                # Extract the acres information
                acres_text = acres.string.strip().replace(',', '')
                # Acres_Num contains my Acres that I need
                acres_num = int(acres_text.split()[0])

                # Print the acres information
                # print(acres_num)
            except AttributeError:
                acres_num = None

            try:
                latitudeAndLongitude = soup.find('strong', string='Location Information').find_next('div').text.strip()
                latitudeAndLongitude = latitudeAndLongitude[21:]
                latitude, longitude = latitudeAndLongitude[1:-1].split(',')
                #Check if it works or not test case use the code below
                # print(latitude)
                # print(longitude)
            except ValueError:
                latitudeAndLongitude = None
                latitude, longitude = None, None

            try:
                cause = soup.find('strong', string='Admin Unit').find_next('div').text.strip()
                if "Cause" in cause:
                    cause = cause[6:]
                    #Check if it works or not test case use the code below
                    # print(cause)
                else:
                    cause = None
            except AttributeError:
                cause = None

            try:
                locationInformation = soup.find('strong', string='Date Contained').find_next('div').text.strip()
                locationInformation = locationInformation[20:]
                locationInformation = f"'{locationInformation}'"
                #Check if it works or not test case use the code below
                # print(locationInformation)
            except AttributeError:
                locationInformation = soup.find('strong', string='Date Started').find_next('div').text.strip()
                locationInformation = locationInformation[20:]
                locationInformation = f"'{locationInformation}'"
                #Check if it works or not test case use the code below
                # print(locationInformation)

            try:
                crewNumber = soup.find("div", class_="factoid__label", string="Crews").find_previous_sibling("div", class_="factoid__data").text.strip()
                #Check if it works or not test case use the code below
                # print(crewNumber)
            except AttributeError:
                crewNumber = None

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

            #Check if it works or not test case use the code below
            # print(numStructuresDamaged)
            # print(numStructuresDestroyed)
            # print(fatality)
            # print(injuries)

            print([NameOfTheFire,county,dateStarted,dateContained,acres_num,
                            latitude,longitude,cause,locationInformation,crewNumber,numStructuresDamaged
                            ,numStructuresDestroyed,fatality,injuries])

            writer.writerow([NameOfTheFire,county,dateStarted,dateContained,acres_num,
                            latitude,longitude,cause,locationInformation,crewNumber,numStructuresDamaged
                            ,numStructuresDestroyed,fatality,injuries])
