import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

path = os.getenv("NBP_API_URL")
def fetch_data(api_url, currency, start_date, end_date):
    try:
        full_url = f"{api_url}/{currency}/{start_date}/{end_date}"
        response = requests.get(full_url)
        if response.status_code == 200:
            data = response.json()
            logging.info(f"Successfully fetched data from {full_url}")
            return data
        else:
            logging.error(f"Failed to fetch data from {full_url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")