import sqlite3
from utils import get_logger

logger = get_logger(__name__)


def save_to_db(df, db_path="../data/nbp.db"):
    conn = sqlite3.connect(db_path)
    logger.info(f"Saving {len(df)} records to database at {db_path}")

    df.to_sql("rates", conn, if_exists="replace", index=False)
    conn.close()

    logger.info("Database update completed successfully")


def save_to_bigquery(df, project_id, dataset_table):
    logger.info(f"Uploading {len(df)} rows to BigQuery table: {dataset_table}...")

    try:
        df.to_gbq(
            destination_table=dataset_table,
            project_id=project_id,
            if_exists="replace"
        )
        logger.info("Data successfully loaded to BigQuery!")
    except Exception as e:
        logger.error(f"Failed to load data to BigQuery: {e}")
        raise e