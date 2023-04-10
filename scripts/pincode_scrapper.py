import json
import requests
import os

from bs4 import BeautifulSoup
from districts import *


for indianState in india:
    state = indianState["state"].replace(" ", "_").lower()
    for district in indianState['districts']:
        district = "".join(remove_space_and_replace_hyphen(district.lower()))

        # Send a GET request to the website
        url = 'https://pincode.india-server.com/cities/{district}/'.format(
            district=district)

        print('url=', url)

        response = requests.get(url)

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the table rows that contain the pincode and place data
        table_rows = soup.select('table tr')

        # Create a list to store the formatted pincode and place data
        formatted_data = []

        # Loop through each table row and extract the pincode and place data
        for row in table_rows:
            cols = row.select('td')
            if len(cols) == 4:
                place = cols[1].get_text().strip()
                pincode = cols[3].get_text().strip()
                formatted_data.append({'place': place, 'pincode': pincode})

        # Checks if the folder is already created else creates it
        path = "../jsons/india/{state}".format(state=state,)
        if not os.path.exists(path):
            print('directory created')
            os.makedirs(path)

        with open("../jsons/india/{state}/{district}.json".format(district=district, state=state), "w") as outfile:
            outfile.write(json.dumps(formatted_data))
    print("state=", state, "district=", len(indianState["districts"]), )
