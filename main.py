from parameters.parameters import (
    data_file_path, linreg_params
)
from data_ingestion.ingest import get_data
from model_building.build_model import linreg_model_build
import time

#linreg_model_build(df_features, df_target, linreg_params)


# Stage 0 - Data Ingestion
print("Starting Data Ingestion")
start_time = time.time()
house_data = get_data(data_file_path)
end_time = time.time()
print(f"Execution time for Data Ingestion is {end_time - start_time} seconds")
print(f"Size of Data is {house_data.shape}")
print(house_data.head())