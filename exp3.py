from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd

# Load data
data = pd.read_csv("data.csv")
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)

# Visualize the Decision Tree
tree.plot_tree(clf, filled=True)
