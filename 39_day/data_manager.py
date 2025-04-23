import os

import requests
from dotenv import load_dotenv

SHEETY_BASE_URL = "https://api.sheety.co/62c23b198adc2a1f97dbcea6c58660a4/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._token = os.getenv("SHEETY_TOKEN")
        self.header = {"Authorization": f"Basic {self._token}"}


    def get_data_from_table(self):
        """
            Retrieves all data from the table via Sheety API.
            return:
                list: A list of dictionaries containing table data (all records from the 'prices' sheet).
        """
        resp = requests.get(url=SHEETY_BASE_URL, headers=self.header).json()
        result = resp["prices"]
        return result


    def add_data_to_table(self,  row_id: int, new_data: dict):
        """
        Updates data in the specified table row via Sheety API.

        Args:
            row_id (int): The ID of the row to update (starting from 1).
            new_data (dict): Dictionary containing new data for the row (ex: {"columnName": "new_value"}).

        Returns:
            dict: API response after updating the data.

        """
        payload = {
            "price": new_data
        }
        resp = requests.put(url=f"{SHEETY_BASE_URL}/{row_id}", headers=self.header, json=payload).json()
        return resp

