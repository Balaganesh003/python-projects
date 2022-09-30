import requests
from flight_search import FlightSearch

GET_API_ENDPOINT = "https://api.sheety.co/420a96e63e25bea8499f2827b87b39ef/flightDealsBala/sheet1"
put_endpoint = "https://api.sheety.co/420a96e63e25bea8499f2827b87b39ef/flightDealsBala/sheet1/[Object ID]"


class Datamanager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=GET_API_ENDPOINT)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_code(self):
        for each_destination in self.destination_data:
            Id = each_destination["id"]
            city = each_destination["city"]
            code = FlightSearch().get_destination_code(city)
            # each_destination["iataCode"] = Flight_search().get_destination_code()

            body = {
                "sheet1": {"iataCode": code

                           }
            }
            response = requests.put(
                url=f"https://api.sheety.co/420a96e63e25bea8499f2827b87b39ef/flightDealsBala/sheet1/{Id}", json=body)
            response.raise_for_status()
        self.destination_data=self.get_destination_data()
