#Fix the training step so the model is trained on the correct training data.


from sklearn.model_selection import train_test_split

X_train, X_test, y_train = train_test_split(X, y, random_state=42, test_size=0.3)
model.fit(X_test, y_train)
