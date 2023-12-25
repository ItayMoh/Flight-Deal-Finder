import os
import requests
from datetime import datetime
from flight_data import FlightData

class FlightSearch:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.KIWI_API = "https://api.tequila.kiwi.com/v2"
        self.KIWI_HEADERS = {
            "apikey": os.environ["KIWI_API_KEY"],
        }

    #Function that is searching an airport IATA code based on the city provided
    def search_airport_iata(self, city):
        search_endpoint = f"https://api.tequila.kiwi.com/locations/query"
        search_parameters = f"term={city}&locale=en-US&location_types=city&limit=10&active_only=true"
        response = requests.get(url=f"{search_endpoint}", params=search_parameters , headers=self.KIWI_HEADERS)
        try:
            airports = response.json()["locations"]
            return airports[0]["code"]

        except:
            print("Something went wrong with requesting the city of the google data sheet")


    def search_flight(self, departed_city_iata,destination_city_iata):
        #Searching a flight from departed city to destination city
        #Returning a flightData object that holds the information about the flight

        #Formatting current date and 6 month later for searching ranges between 0-6 months of flights
        date_from = datetime.today().strftime("%d/%m/%Y")
        six_month_further = datetime.today().strftime("%m")
        current_year = datetime.today().strftime("%Y")
        if(int(six_month_further) + 6 > 12):
            six_month_further = str((int(six_month_further) + 6) %13)
            current_year = str(int(current_year) + 1)
        else:
            six_month_further = str(int(six_month_further) + 6)


        date_to = datetime.today().strftime(f"%d/{six_month_further}/{current_year}")

        #Searching parameters for the flight
        parameters = {
            "fly_from": f"{departed_city_iata}",
            "fly_to": f"{destination_city_iata}",
            "date_from": f"{date_from}",
            "date_to":f"{date_to}",
            "curr":"USD",
            "sort":"price",
            "nights_in_dst_from": 7,
            "nights_in_dst_to":28,
            "one_for_city": 1

        }

        response = requests.get(url=f"{self.KIWI_API}/search", params=parameters, headers=self.KIWI_HEADERS)
        try:
            data = response.json()["data"][0]
        except:
            print(f"Flight not found to destination {destination_city_iata} from {departed_city_iata}")

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["cityCodeTo"],
            out_date=data["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data