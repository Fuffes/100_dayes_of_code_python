

class FlightData:

    def __init__(self, all_flights: dict):
        self._all_flights = all_flights
        self._all_flights_data = self.get_necessary_data()
        # self.origin = all_flights[0]

    def get_necessary_data(self):
        necessary_data = []
        flights_list = self._all_flights["data"]
        for flight in flights_list:
            if flight:
                data = {"from": flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                        "to": flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                        "departure_time": flight["itineraries"][0]["segments"][0]["departure"]["at"],
                        "price": float(flight["price"]["base"]),
                        "currency": flight["price"]["currency"],
                        }
                necessary_data.append(data)
        return necessary_data

    def find_cheapest_flights(self):
        try:
            min_price = min(float(f['price']) for f in self._all_flights_data)
            cheapest_flights = [f for f in self._all_flights_data if float(f['price']) == min_price]
            return cheapest_flights
        except ValueError:
            pass
