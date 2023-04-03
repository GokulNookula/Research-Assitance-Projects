from bs4 import BeautifulSoup
import requests
import csv

#Insert the Url Link where you want to extract the stuff from
url = '"#insert url here"'

#Change the reference page when your trying to access different years from the above website or you will get Forbidden Acess aka <Response [403]
headers = {
    'User-Agent': '#Put your user agent by typing my user agent in the whaterver web browser your using',
    'Referer': '#give a reference here'
}

response = requests.get(url,headers=headers)

if (response.status_code == 200):
    soup = BeautifulSoup(response.content, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link["href"])

    # write to csv file
    with open("done.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows([[link] for link in links])
