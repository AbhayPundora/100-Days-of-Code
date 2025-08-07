#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from  flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint
from notification_manager import NotificationManager


#fetching the sheet data
flight_data = FlightData()
flight_data.fetch_flight_data()
sheet_data = flight_data.flight_data
pprint(sheet_data)

flight_search = FlightSearch()


#adding the iataCode in sheet_data             -------------------------------------
# flight_search.set_flight_data(sheet_data)                                         |

# complete_sheet_data = flight_search.complete_data                                 | --------this only need for putting right itea code to the sheet so we don't need after running for on time

# #setting the iataCode for each airport in google sheet via put req.               |
# data_manager = DataManager()                                                      |
# data_manager.set_iata_code(complete_sheet_data) -----------------------------------

check_flight_data = flight_search.search_cheapest_flight()

notification_manager = NotificationManager()
notification_manager.compare_price(sheet_data, check_flight_data)

