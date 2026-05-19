import pandas_gbq
from utils import get_logger

logger = get_logger(__name__)


def save_to_bigquery(df, project_id, dataset_table):
    logger.info(f"Uploading {len(df)} rows to BigQuery ({dataset_table})...")

    try:
        pandas_gbq.to_gbq(
            dataframe=df,
            destination_table=dataset_table,
            project_id=project_id,
            if_exists="replace",
        )
        logger.info("Data successfully loaded to BigQuery!")
    except Exception as e:
        logger.error(f"Failed to load data to BigQuery: {e}")
        raise e
