from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# Load data
data = pd.read_csv("data.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predict on a new sample
sample = [[...]]  # Provide sample feature values
print("Prediction for new sample:", knn.predict(sample))
