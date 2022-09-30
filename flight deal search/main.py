from datetime import *

from data_manager import Datamanager
from flight_search import FlightSearch

datamanager = Datamanager()
sheet_data = datamanager.get_destination_data()
datamanager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
flightsearch = FlightSearch()
for each_destination in datamanager.destination_data:
    data = flightsearch.check_flights("LON", each_destination["iataCode"], tomorrow, six_month_from_today)
    print(data)
