import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and fit the LDA model
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)

# Transform the test data to LDA dimensions
X_test_lda = lda.transform(X_test)

# Make predictions on the test data
y_pred = lda.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)

# Create a scatter plot to visualize the LDA dimensions
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], data.target_names):
    plt.scatter(X_test_lda[y_test == i, 0], X_test_lda[y_test == i, 1], alpha=.8, color=color,
                label=target_name)

# Add labels, a legend, and a title to the plot
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')

# Display accuracy on the plot
plt.text(2.5, 2.5, f'Accuracy: {accuracy:.2f}', fontsize=12)

plt.show()
