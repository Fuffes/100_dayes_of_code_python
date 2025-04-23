from dotenv import load_dotenv
from data_manager import DataManager

load_dotenv()

# Program Requirements

# TODO 1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA)
#  codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).


# TODO 2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# TODO 3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.


# TODO 4. The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.






dm = DataManager()
data = dm.get_data_from_table()

for city in data:
    if city["iataCode"] == " ":
        code = 'test'
        new_data = {"iataCode": code}
        dm.add_data_to_table(row_id=city["id"], new_data=new_data)








# from datetime import datetime, timedelta
#
# from flight_search import FlightSearch
# from data_manager import dd
#
#
# origin = "WAW"
# fs = FlightSearch()
# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
