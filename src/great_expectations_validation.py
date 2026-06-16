import pandas as pd
import great_expectations as gx


DATA_PATH = "data/raw/transactions.csv"

data = pd.read_csv(DATA_PATH)

context = gx.get_context()

data_source = context.data_sources.add_pandas(
    name="transactions_pandas_source"
)

data_asset = data_source.add_dataframe_asset(
    name="transactions_dataframe_asset"
)

batch_definition = data_asset.add_batch_definition_whole_dataframe(
    name="transactions_batch"
)

batch = batch_definition.get_batch(
    batch_parameters={"dataframe": data}
)

validator = context.get_validator(
    batch=batch
)

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

result = validator.validate()

if result.success:
    print("Great Expectations validation passed")
else:
    print("Great Expectations validation failed")
    print(result)