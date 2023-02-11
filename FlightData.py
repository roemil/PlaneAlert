from FlightRadar24.api import FlightRadar24API

class FlightData:
    def __init__(self):
        self.fr_api = FlightRadar24API()
    
    def setZone(self, zone):
        self.zone = zone
    
    def run(self):
        bounds = self.fr_api.get_bounds(self.zone)
        flights = self.fr_api.get_flights(bounds = bounds)
        data = []
        for flight in flights:
            details = self.fr_api.get_flight_details(flight.id)
            tmp = {
                "aircraft" : details["aircraft"]["model"]["text"],
                "origin" : flight.origin_airport_iata,
                "destination" : flight.destination_airport_iata,
                "callsign" : flight.callsign
            }
            data.append(tmp)
        return data