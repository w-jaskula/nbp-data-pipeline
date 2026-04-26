from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def safe_get(dictionary, key, default=None):
    return dictionary.get(key, default)