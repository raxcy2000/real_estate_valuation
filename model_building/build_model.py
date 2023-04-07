import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib



def perform_train_test_split(df_features, df_target):
    X_train, X_test, y_train, y_test = (
        train_test_split(df_features, df_target, test_size=0.25, random_state=42)
        )

    # train_data, test_data = (
    #     train_test_split(df, test_size=0.33, random_state=42)
    # )
    # return train_data, test_data
    return X_train, X_test, y_train, y_test


def linreg_model_build(df_features, df_target, linreg_params):
    save_path = linreg_params["save_path"]

    X_train, X_test, y_train, y_test = perform_train_test_split(
        df_features, df_target)

    model = LinearRegression(fit_intercept=False).fit(X_train, y_train)

    filename = os.path.join(save_path,'finalized_model.pkl')
    joblib.dump(model, filename)

    return X_test, y_test, filename 


def evaluator(X_test, y_test, filename):
    '''
    load the model 
    '''
    loaded_model = joblib.load(filename)
    predicted = loaded_model.predict(X_test)
    result = mean_squared_error(y_test,predicted)

    return result
