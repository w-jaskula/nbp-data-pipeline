# Draft
from extract import fetch_data
from transform import clean_data
from load import save_to_csv

def main():
    data = fetch_data(...)
    clean = clean_data(data)
    save_to_csv(clean, ...)

if __name__ == "__main__":
    main()