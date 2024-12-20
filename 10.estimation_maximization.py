import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Generate synthetic data
np.random.seed(42)
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)

# Visualize the original data points
plt.scatter(X[:, 0], X[:, 1], c=y_true, s=40, cmap='viridis', marker='o', edgecolor='k')
plt.title("Original Data with True Labels")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Apply Gaussian Mixture Model using the EM algorithm
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X)
y_gmm = gmm.predict(X)

# Performance Evaluation: Calculate Silhouette Score
silhouette_avg = silhouette_score(X, y_gmm)
print(f"Silhouette Score for GMM clustering: {silhouette_avg:.2f}")

# Visualize the clusters found by EM
plt.scatter(X[:, 0], X[:, 1], c=y_gmm, s=40, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(gmm.means_[:, 0], gmm.means_[:, 1], c='red', s=100, marker='x', label='Cluster Centers')
plt.title("GMM Clustering with EM Algorithm")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
