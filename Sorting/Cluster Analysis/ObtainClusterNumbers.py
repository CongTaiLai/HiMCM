from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score

data = load_iris()
X = data.data

# elbow method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

fig, ax = plt.subplots(2)

ax[0].plot(range(1, 11), wcss)
ax[0].set_title('Elbow Method')
ax[0].set_xlabel('Number of clusters')
ax[0].set_ylabel('WCSS')

# Silhouette Score
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    # ax[1].scatter(k, score, color="blue")
    silhouette_scores.append(score)

# Find the k with the highest silhouette score
best_k = silhouette_scores.index(max(silhouette_scores)) + 2  # +2 because k starts from 2

print(silhouette_scores)
print(f'Best number of clusters (k) according to Silhouette Score: {best_k}')

plt.show()
