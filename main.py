from parameters.parameters import (
    data_file_path, linreg_params
)
from data_ingestion.ingest import get_data
from model_building.build_model import linreg_model_build, evaluator


# Stage 0 - Data Ingestion
print("Starting Data Ingestion")

house_data = get_data(data_file_path)
print(house_data.head())


features = house_data.iloc[:,:-1]
target = house_data.iloc[:,-1]
print(f"Shape of features is {features.shape}")
print(f"Shape of target is {target.shape}")


X_test, y_test, filename = linreg_model_build(
    features, target, linreg_params
    )

result = evaluator(X_test, y_test, filename)
print(f"Mean_Squared_Error is {result}")