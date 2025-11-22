# Write a function that splits a dataset into train, validation, and test sets manually using slicing (cannot use sklearn).
import numpy as np

def data_split(X, y, train=0.8, val=0.1, test=0.1):
    data = np.column_stack((X, y))
    return (X_train, y_train, X_validation, y_validation, X_test, Y_test)
