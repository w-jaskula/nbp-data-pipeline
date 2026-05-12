import sqlite3
from utils import get_logger

logger = get_logger(__name__)

def save_to_db(df, db_path="../data/nbp.db"):
    conn = sqlite3.connect(db_path)

    logger.info(f"Saving {len(df)} records to database at {db_path}")

    df.to_sql("rates", conn, if_exists="replace", index=False)
    conn.close()

    logger.info("Database update completed successfully")