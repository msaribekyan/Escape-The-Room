# Write a function that standardizes only the numeric columns of a pandas DataFrame (ignoring categorical ones).

# Note: Use df.select_dtypes and StandardScaler

import pandas as pd
from sklearn.preprocessing import StandardScaler

def normalize_df(df):
    num_cols = df.select_dtypes(include=['float', 'int']).columns
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df

data = {
   'A': [1, 2, 3],
    'B': [4, 4, 10],
    'C': [7, 8, 9],
    'D': [3, 3, 3],
    "E": ['hello', 'hi', 'hey']
}

df = pd.DataFrame(data)

print(normalize_df(df))
