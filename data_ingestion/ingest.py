import pandas as pd

def get_data(f):
    """
    This is a function that takes a file path and read in data
    with pandas
    : f: filepath
    : df: resulting data
    """
    if f.endswith('.csv'):
        df = pd.read_csv(f)
    elif f.endswith('.xlsx'):
        df = pd.read_excel(f)
    else:
        print("Can only read in '.csv' or '.xlsx' files")

    return df

def get_feature_target(data):
    features = data.iloc[:,:-1]
    target = data.iloc[:,-1]
    print(f"Shape of features is {features.shape}")
    print(f"Shape of target is {target.shape}")

    return features, target