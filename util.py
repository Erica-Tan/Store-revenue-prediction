import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

# prepare encoding funbction
def transform_datetime(X_data, column):
    # extract datetime features for training set
    df_date = pd.to_datetime(X_data[column], 
                         format = '%d/%m/%Y', 
                         errors = 'coerce')
    X_data['createdDateYear'] = df_date.dt.year
    X_data['createdDateMonth'] = df_date.dt.month
    X_data['createdDateDay'] = df_date.dt.day
    X_data = X_data.drop(column, axis=1)
    return X_data

# prepare encoding funbction
def scale_features(X_train, X_valid, columns):
    scaler = StandardScaler()
    scaler.fit(X_train[columns])
    X_train.loc[:,columns] = scaler.transform(X_train[columns])
    X_valid.loc[:,columns] = scaler.transform(X_valid[columns])
    return X_train, X_valid

# prepare encoding funbction
def encode_catogory_features(X_train, X_valid, columns):
    oe = OrdinalEncoder()
    oe.fit(X_train[columns])
    X_train.loc[:,columns] = oe.transform(X_train[columns])
    X_valid.loc[:,columns] = oe.transform(X_valid[columns])
    return X_train, X_valid