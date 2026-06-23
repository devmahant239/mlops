import logging 
import pandas as pd 
import great_expectations as gx

logging.basicConfig(level=logging.INFO)

RAW_DATA_PATH = "data/raw/transactions.csv"

def load_raw_data():
    data = pd.read_csv(RAW_DATA_PATH)
    logging.info("raw dataset is loaded for greate expectation validation")
    return data

def create_validator(data):
    context = gx.get_context()

    data_source = context.data_sources.add_pandas(
        name="transaction_pandas_source"
    )

    data_asset = data_source.add_dataframe_asset(
        name="transaction_dataframe_asset"
    )

    batch_definition = data_asset.add_batch_definition_whole_dataframe(
        name = "transiction_batch"
    )

    batch = batch_definition.get_batch(
        batch_parameters={"dataframe": data}
    )

    validator = context.get_validator(
        batch=batch
    )

    return validator

def add_expectation(validator):
    validator.expect_column_to_exist("transaction_id")
    validator.expect_column_to_exist("amount")
    validator.expect_column_to_exist("location")
    validator.expect_column_to_exist("transaction_type")
    validator.expect_column_to_exist("transaction_time")
    validator.expect_column_to_exist("is_fraud")

    validator.expect_column_values_to_not_be_null("transaction_id")
    validator.expect_column_values_to_not_be_null("amount")

    validator.expect_column_values_to_be_between(
        "amount",
        min_value=1
    )

    validator.expect_column_values_to_be_in_set(
        "transaction_type",
        ["atm", "online", "pos", "bank_transfer"]
    )
    
    
    logging.info("Greate Expectation rules added succesfully")

def run_great_expectations_validation():
    logging.info("Great expectation validation started")

    data = load_raw_data()

    validator = create_validator(data)

    add_expectation(validator)

    result = validator.validate()

    if result.success:
        logging.info("Great expectation validation passed")
    else:
        logging.error("Great expectation validation failed")
        raise ValueError(result)
    
    logging.info("great Expectation validation completed")

if __name__ == "__main__":
    run_great_expectations_validation()
