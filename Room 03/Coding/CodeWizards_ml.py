# Using scikit-learn, create a complete machine learning pipeline that: loads the Iris dataset; applies StandardScaler for feature scaling; trains a Logistic Regression model; uses GridSearchCV to find the best value for the C parameter (regularization strength); prints the best hyperparameters and the model's accuracy on a test set.

# Note: GridSearchCV helps find the best model parameters automatically.

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load data
X, y = load_iris(return_X_y=True)

# feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# grid search
grid_search = GridSearchCV(LogisticRegression(), {
    'C': [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100],
}, cv=5, return_train_score=True)

# prepare data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, 
        test_size=0.2, random_state=42
)

# train model
grid_search.fit(X_train,y_train)

# evaluate the accuracy
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# print results
print("Best hyperparameters: ", grid_search.best_params_)
print("Accuracy: ", accuracy_score(y_test, y_pred))
