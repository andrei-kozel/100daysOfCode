from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

sheet_data = manager.get_data()

if sheet_data[0]["iataCode"] == "":
    for flight in sheet_data:
        response = flight_search.get_destination_code(flight["city"])
        flight["iataCode"] = response

    sheet_data = manager.update_sheet(sheet_data)

for flight in sheet_data:
    price = flight_data.get_flight_data((flight["iataCode"]))
    print(f"{flight['city']}: {price}")
