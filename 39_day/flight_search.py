import os

import requests

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        self._access_token = self._get_access_token()
        self._auth_header = {"Authorization" : f"Bearer {self._access_token}"}

    def get_code(self, city_name, ):
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=self._auth_header, params=query)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def _get_access_token(self):
        """
            Generates the authentication token used for accessing the Amadeus API and returns it.
            Returns:
                str: The new access token obtained from the API response.
        """
        auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        api_key = os.getenv("FLIGHT_SEARCH_API_KEY")
        api_secret = os.getenv("FLIGHT_SEARCH_API_SECRET")
        header = {"Content-Type":"application/x-www-form-urlencoded"}
        body = f"grant_type=client_credentials&client_id={api_key}&client_secret={api_secret}"

        resp = requests.post(url=auth_url, headers=header, data=body )
        resp.raise_for_status()
        access_token = resp.json()["access_token"]
        return access_token

    def get_flight_data(self, destination, origin, from_time, to_time):
        """
        """
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": "10",
        }
        resp = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=self._auth_header).json()
        return resp
