from sklearn.neural_network import MLPClassifier
import pandas as pd

# Load data
data = pd.read_csv("data.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Initialize and train the model
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
mlp.fit(X, y)

# Predict on a new sample
sample = [[...]]  # Provide sample feature values
print("Prediction for new sample:", mlp.predict(sample))
