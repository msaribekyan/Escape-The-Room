# Write a function that splits a dataset and manually balances the training set for equal class representation.

import pandas as pd

def data_split(data, target, train=0.8):
    train_data = []
    test_data = []

    classes = data[target].unique()
    
    for cls in classes:
        class_data = data[data[target] == cls]
        class_data = class_data.sample(frac=1, random_state=42).reset_index(drop=True)
        size = int(len(class_data) * train)
        class_train = class_data[:size]
        class_test = class_data[size:]
        train_data.append(class_train)
        test_data.append(class_test)
    
    data_train = pd.concat(train_data).reset_index(drop=True)
    data_test = pd.concat(test_data).reset_index(drop=True)
    
    return (data_train,  data_test)

# from sklearn.datasets import load_iris
# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df['target'] = iris.target
# print(data_split(df, "target", 0.8))
