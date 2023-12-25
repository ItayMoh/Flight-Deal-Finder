import os
import requests

#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.cities = []
        self.google_sheet_data = {}



        #Authentication url/headers for Sheety api
        self.GOOGLE_SHEET_PRICE_COMPARE_URL = os.environ["GOOGLE_SHEET_PRICE_COMPARE_URL"]
        self.SHEETY_AUTHORIZATION_HEADERS = {
            'Content-Type': 'application/json',
            "Authorization": os.environ["SHEETY_AUTHORIZATION"]
        }
        self.flight_template_google_sheet = {
            "price":{
                "city": "",
                "iataCode": "",
                "lowestPrice": "",
            }
        }

        try:
            response = requests.get(url=self.GOOGLE_SHEET_PRICE_COMPARE_URL, headers=self.SHEETY_AUTHORIZATION_HEADERS)
        except:
            print("Something went wrong with receiving data from google sheet")
        else:
            self.google_sheet_data = response.json()["prices"]


    def get_google_sheet_cities(self):
        #Assign the google sheet cities into the cities array property and retriving the google sheet data
        try:
            #Getting each city from the data sheet
            for row in self.google_sheet_data:
                self.cities.append(row["city"])

        except:
            print("Something went wrong with retrieving information from the google sheet")

    def update_column_in_sheet(self, update_field):

        for city in self.google_sheet_data:
            update_data = {
                "price": {
                    update_field: city[f"{update_field}"]
                }
            }

            response = requests.put(url=f"{self.GOOGLE_SHEET_PRICE_COMPARE_URL}/{city['id']}",
                                    json=update_data)

