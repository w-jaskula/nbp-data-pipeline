import os
import pandas as pd
from dotenv import load_dotenv
from extract import fetch_data
from transform import transform_data
from load import save_to_db
from utils import get_logger

load_dotenv()
logger = get_logger(__name__)

def main():
    logger.info("Starting NBP Currency Pipeline")
    api_url = os.getenv("NBP_API_URL")

    logger.info("Fetching data for EUR, USD, and GBP...")
    eur_data = fetch_data(api_url, "EUR", "2026-01-01", "2026-03-31")
    usd_data = fetch_data(api_url, "USD", "2026-01-01", "2026-03-31")
    gbp_data = fetch_data(api_url, "GBP", "2026-01-01", "2026-03-31")

    df_eur = transform_data(eur_data)
    df_usd = transform_data(usd_data)
    df_gbp = transform_data(gbp_data)

    logger.info("Merging datasets and saving to database...")
    df = pd.concat([df_eur,df_usd,df_gbp])
    save_to_db(df, "../data/nbp.db")

    logger.info("Pipeline finished successfully")

if __name__ == "__main__":
    main()