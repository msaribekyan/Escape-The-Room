# Write a function standardize_and_classify(df) that accepts a pandas DataFrame with numerical columns ["A", "B"] and target column "label"; standardizes the columns ["A", "B"] using StandardScaler; fits a LogisticRegression model to classify "label", returns the model's training accuracy using .score()

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def standardize_and_classify(df):
    scaler = StandardScaler()
    df[["A", "B"]] = scaler.fit_transform(df[["A", "B"]])
    X = df[["A", "B"]]
    y = df["label"]
    model = LogisticRegression()
    model.fit(X, y)
    return model.score(X, y)

data = {
   "A":     [1, 2, 3, 4, 5],
   "B":     [4, 4, 10, 2, 3],
   "label": ['yes', 'no', 'no', 'yes', 'no']
}

df = pd.DataFrame(data)

print(standardize_and_classify(df))
