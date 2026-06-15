import logging
import pandas as pd


logging.basicConfig(level=logging.INFO)


RAW_DATA_PATH = "data/raw/transactions.csv"


def load_data():
    data = pd.read_csv(RAW_DATA_PATH)

    logging.info("raw data loaded successfully")

    return data


def validate_required_columns(data):
    required_columns = [
        "transaction_id",
        "amount",
        "location",
        "transaction_type",
        "transaction_time",
        "is_fraud"
    ]

    missing_columns = []

    for column in required_columns:
        if column not in data.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(f"missing required columns: {missing_columns}")

    logging.info("required columns validation passed")


def validate_missing_values(data):
    missing_values = data.isnull().sum()

    if missing_values.sum() > 0:
        raise ValueError(f"missing values found:\n{missing_values}")

    logging.info("missing values validation passed")


def validate_amount(data):
    invalid_amounts = data[data["amount"] <= 0]

    if not invalid_amounts.empty:
        raise ValueError("amount validation failed: amount must be greater than 0")

    logging.info("amount validation passed")


def run_validation_pipeline():
    logging.info("data validation started")

    data = load_data()

    validate_required_columns(data)
    validate_missing_values(data)
    validate_amount(data)

    logging.info("data validation completed successfully")


if __name__ == "__main__":
    run_validation_pipeline()