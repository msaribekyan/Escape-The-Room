# Write a function that splits a dataset into train, validation, and test sets manually using slicing (cannot use sklearn).
import pandas as pd

def data_split(data, train=0.8, val=0.1, test=0.1):
    if(train+val+test != 1):
        return (data)

    data = data.sample(frac=1)

    total_rows = data.shape[0]
    train_size = int(total_rows*train)
    validation_size = int(total_rows*val)

    data_train = data[0:train_size]
    data_validation = data[train_size:(train_size+validation_size)]
    data_test = data[(train_size+validation_size):]
    
    return (data_train, data_validation, data_test)
