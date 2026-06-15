import pandas as pd
import logging 
from database import get_connection

logging.basicConfig(level=logging.INFO)

RAW_DATA_PATH = "data/raw/transactions.csv"

def extract_transaction():
    connection = get_connection()

    query = "SELECT * FROM transactions"

    data = pd.read_sql(
        query,
        connection
    )
    connection.close()

    return data


def save_raw_data(data):
    data.to_csv(
        RAW_DATA_PATH,
        index=False
    )
    logging.info(f"raw data saved succesfully at {RAW_DATA_PATH}")


def run_extraction_pipeline():
    logging.info("data extraction started")

    data = extract_transaction()
    logging.info(f"extracted {len(data)} records from postgress")
    save_raw_data(data)

    logging.info("data extraction completed")

if __name__ == "__main__":
    run_extraction_pipeline()



