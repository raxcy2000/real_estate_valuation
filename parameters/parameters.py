import os

DATASET_NAME = "Real_estate_valuation_dataset.xlsx"

DATA_FOLDER = "data"
main_path = os.getcwd()

data_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), DATASET_NAME)

linreg_params = {
    "save_path": 'artifacts/models_regression'
}