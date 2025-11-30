#Fix the order of operations and ensure the model is trained using proper data structures before prediction.

import numpy as np
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
X = np.array([
    [0.1, 0.2],
    [0.3, 0.4]
])
y = np.array([0, 1])

model.fit(X, y)
model.predict(X)
