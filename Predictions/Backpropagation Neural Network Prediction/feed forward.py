import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
X = np.linspace(0, 1, 100)
y = 2 * X + 1 + 0.1 * np.random.randn(100)

# Create a feedforward neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Input layer with one input feature
    tf.keras.layers.Dense(10, activation='relu'),  # Hidden layer with 10 neurons and ReLU activation
    tf.keras.layers.Dense(1)  # Output layer with one neuron (for regression)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Make predictions
X_test = np.linspace(0, 1, 50)
y_pred = model.predict(X_test)

# Plot the original data and the neural network predictions
plt.scatter(X, y, label='Data', color='blue')
plt.plot(X_test, y_pred, label='Predictions', color='red', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
