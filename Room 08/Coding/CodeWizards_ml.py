# Write a function that calculates the mean and standard deviation for each numeric column in a pandas DataFrame.

import pandas as pd

def mean_std(df):
    result = {}
    for col in df.columns:
        # Check if it contains non-numbers
        if (not pd.to_numeric(df[col], errors='coerce').notnull().all()):
            continue
        result[col] = (df[col].mean(), df[col].std())
    return result

data = {
   'A': [1, 2, 3],
    'B': [4, 4, 10],
    'C': [7, 8, 9],
    'D': [3, 3, 3],
}

df = pd.DataFrame(data)

print(mean_std(df))
