import data_manager
import flight_search
import notification_manager

ORIGIN_COUNTRY_IATA = "TLV"

#Object creations
data_manager_obj = data_manager.DataManager()
flight_search_obj = flight_search.FlightSearch()
notification_manager_obj = notification_manager.NotificationManager()
#Retrieving cities from the google sheet into data_manager property a mnrray
data_manager_obj.get_google_sheet_cities()


#Get iataCodes if the iataCodes doesn't exist
if(data_manager_obj.google_sheet_data[0]["iataCode"] == ""):
    #Returning IATA code for each city in the google data sheet
    for city in data_manager_obj.google_sheet_data:
        city["iataCode"] = flight_search_obj.search_airport_iata(city["city"])

    print("Writing iata codes to google docs")
    data_manager_obj.update_column_in_sheet("iataCode")

#Checking If there is a cheaper price than the price in the google data sheet
for city in data_manager_obj.google_sheet_data:
    print(city)
    flight_obj = flight_search_obj.search_flight(ORIGIN_COUNTRY_IATA, city["iataCode"])
    #Check for available lowest number, send sms if there is and update the price field in the google sheet
    if(city["lowestPrice"] > flight_obj.price):
        notification_manager_obj.send_msg(f"We found a cheaper deal to {flight_obj.destination_city} for {flight_obj.price}$ instead of {city['lowestPrice']}$")
        city["lowestPrice"] = flight_obj.price
        data_manager_obj.update_column_in_sheet("lowestPrice")