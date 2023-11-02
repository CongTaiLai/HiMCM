import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Create a synthetic dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create individual decision tree classifiers
tree1 = DecisionTreeClassifier(max_depth=3, random_state=42)
tree2 = DecisionTreeClassifier(max_depth=5, random_state=42)
tree3 = DecisionTreeClassifier(max_depth=7, random_state=42)

# Create an ensemble of decision trees
ensemble = VotingClassifier(estimators=[('tree1', tree1), ('tree2', tree2), ('tree3', tree3)], voting='hard')

# Train the ensemble model
ensemble.fit(X_train, y_train)

# Create a mesh grid to visualize the decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))

# Predict class labels for each point in the mesh grid
Z = ensemble.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='o', edgecolor='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Ensemble Decision Boundary')
plt.show()

print(accuracy_score(y_test, ensemble.predict(X_test)))
