import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create a simple dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Reshape the data (necessary when you have a single feature)
x = x.reshape(-1, 1)

# Create and fit a linear regression model
model = LinearRegression()
model.fit(x, y)

# Make predictions
x_pred = np.array([6, 7, 8])
x_pred = x_pred.reshape(-1, 1)
y_pred = model.predict(x_pred)

# Visualize the original data and the regression line
plt.scatter(x, y, label='Data Points', color='red')
plt.plot(x_pred, y_pred, label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Linear Regression')
plt.show()

print("Predicted values for x_pred:", y_pred)
