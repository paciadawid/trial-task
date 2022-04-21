import json

import requests

from config import DATA_ENDPOINT


def get_locales(country, file_location=None) -> tuple[str, str, str]:
    if file_location:
        with open(file_location, "r") as file:
            response_json = json.load(file)
    else:
        response_json = requests.get(DATA_ENDPOINT).json()
    for hit in response_json["hits"]:
        if hit["locale"].upper() == country.upper():
            base_url = hit["data"]["baseUrl"]
            specialization, location = hit["data"]["searchData"].values()
            city = location.split(',')[0]

            return base_url, specialization, city
