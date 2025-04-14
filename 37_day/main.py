import os

import requests
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

BASE_URL = "https://pixe.la/v1"
GRAPH_ID = "g1"
today = datetime.now().strftime("%Y%m%d")
header = {"X-USER-TOKEN": TOKEN}


# CREATE USER
def create_pixela_user():
    params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    resp = requests.post(url=f"{BASE_URL}/users", json=params)
    return resp.status_code


# CREATE GRAPH
def create_graph():
    graph_config = {
        "id" : GRAPH_ID,
        "name" : "English Graph" ,
        "unit" : "h" ,
        "type" : "float",
        "color" : "ajisai",
    }
    resp = requests.post(url=f"{BASE_URL}/users/{USERNAME}/graphs", json=graph_config, headers=header )
    return resp.status_code

def add_pixel():
    graph_config = {
        "date" : today,
        "quantity" : "1.0",
    }
    resp = requests.post(url=f"{BASE_URL}/users/{USERNAME}/graphs/{GRAPH_ID}", json=graph_config, headers=header )
    return resp.status_code



def update_pixel():
    graph_config = {
        "quantity": "100.0",
    }
    resp = requests.put(url=f"{BASE_URL}/users/{USERNAME}/graphs/{GRAPH_ID}/{today}", json=graph_config, headers=header)
    return print(resp.text)


def delete_pixel():
    resp = requests.delete(url=f"{BASE_URL}/users/{USERNAME}/graphs/{GRAPH_ID}/{today}",
                           headers=header)
    return print(resp.text)

