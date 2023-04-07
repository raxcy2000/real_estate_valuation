from parameters.parameters import (
    data_file_path, linreg_params
)
from data_ingestion.ingest import get_data, get_feature_target
from model_building.build_model import linreg_model_build, evaluator


print("Starting Data Ingestion")

house_data = get_data(data_file_path)
print(house_data.head())

features, target = get_feature_target(house_data)

X_test, y_test, filename = linreg_model_build(
    features, target, linreg_params
    )

result = evaluator(X_test, y_test, filename)
print(f"Mean_Squared_Error is {result}")