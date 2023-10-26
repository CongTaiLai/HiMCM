import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()
X = data.data  # Features (sepal length, sepal width, petal length, petal width)

# We're interested in the first two features (sepal length and sepal width)
X_sepal = X[:, :2]

# Perform K-Means clustering with a specified number of clusters (k)
k = 3  # You can adjust the number of clusters as needed
kmeans = KMeans(n_clusters=k)
kmeans.fit(X_sepal)

# Get cluster labels and centroids
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Plot the clusters
plt.figure(figsize=(8, 6))
colors = ['b', 'g', 'r']  # Color for each cluster

for i in range(k):
    cluster_points = X_sepal[cluster_labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {i + 1}')

# Plot cluster centers
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='k', marker='x', s=100, label='Centroids')

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering of Iris Flowers (Sepal Length vs. Sepal Width)')
plt.legend()
plt.show()
