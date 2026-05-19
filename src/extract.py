import requests
from utils import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger(__name__)


def fetch_data(api_url, currency, start_date, end_date):
    try:
        full_url = f"{api_url}/{currency}/{start_date}/{end_date}"
        response = requests.get(full_url)
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Successfully fetched data from {full_url}")
            return data
        else:
            logger.error(f"Failed to fetch data from {full_url}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")
