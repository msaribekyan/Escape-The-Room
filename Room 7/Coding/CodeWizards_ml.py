# Write a function that normalizes a pandas DataFrame per column, skipping columns with constant values.

import pandas as pd

def normalize_df(df):
    for col in df.columns:
        # Check if it contains non-numbers
        if (not pd.to_numeric(df[col], errors='coerce').notnull().all()):
            continue
        # Check of the column is constant
        if (df[col].nunique() == 1):
            continue
        df[col] = (df[col]-df[col].mean())/df[col].std()

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
