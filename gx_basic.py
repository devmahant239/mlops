import pandas as pd 
import great_expectations as gx

data = pd.DataFrame(
    {
        "name": ["dev","raj","alex"],
        "age":[25,30,28]
    }
)

context = gx.get_context()

data_source = context.data_sources.add_pandas(
    name="my_source"
)

data_asset = data_source.add_dataframe_asset(
    name= "people_data"
)

batch_definition = data_asset.add_batch_definition_whole_dataframe(
    name = "first_batch"
)

batch = batch_definition.get_batch(
    batch_parameters={
        "dataframe": data
    }
)

validator = context.get_validator(
    batch=batch
)
validator.expect_column_to_exist(
    "age"
)

result = validator.validate()

print(result.success)