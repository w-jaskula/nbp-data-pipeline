# Jeśli funkcja odpowiada na pytanie:
# „CO robimy?” → nie utils
# „JAK pomagamy to zrobić?” → utils

# formatowanie danych
def normalize_text(text):
    return text.strip().lower()

# parsowanie dat
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

# bezpieczne pobieranie z dict
# (API często ma braki!)

def safe_get(dictionary, key, default=None):
    return dictionary.get(key, default)

# helper do logowania
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

# walidacja danych
def is_valid_salary(value):
    return value is not None and value > 0