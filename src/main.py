import os
from dotenv import load_dotenv
from extract import fetch_data
from transform import transform_data
from load import save_to_csv

load_dotenv()

def main():
    api_url = os.getenv("NBP_API_URL")

    data = fetch_data(api_url, "EUR", "2026-01-01", "2026-03-31")
    df = transform_data(data)
    save_to_csv(df, "../data/nbp_data.csv")

if __name__ == "__main__":
    main()