import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import BayesianRidge

# Generate some sample data
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.normal(0, 1, 100)  # Simulating noisy linear data

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Linear Regression
axs[0, 0].scatter(x, y, label='Data', color='red')
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))
axs[0, 0].plot(x, y_pred, label='Linear Regression', linestyle='--')
axs[0, 0].set_title('Linear Regression')

# Ridge Regression
axs[0, 1].scatter(x, y, label='Data', color='red')
model = Ridge(alpha=1.0)
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))
axs[0, 1].plot(x, y_pred, label='Ridge Regression', linestyle='--')
axs[0, 1].set_title('Ridge Regression')

# Lasso Regression
axs[0, 2].scatter(x, y, label='Data', color='red')
model = Lasso(alpha=1.0)
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))
axs[0, 2].plot(x, y_pred, label='Lasso Regression', linestyle='--')
axs[0, 2].set_title('Lasso Regression')

# SVR (Support Vector Regression)
axs[1, 0].scatter(x, y, label='Data', color='red')
model = SVR(kernel='linear', C=1.0, epsilon=0.2)
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))
axs[1, 0].plot(x, y_pred, label='Support Vector Regression', linestyle='--')
axs[1, 0].set_title('SVR')

# Random Forest Regression
axs[1, 1].scatter(x, y, label='Data', color='red')
model = RandomForestRegressor(n_estimators=10, random_state=0)
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))
axs[1, 1].plot(x, y_pred, label='Random Forest Regression', linestyle='--')
axs[1, 1].set_title('Random Forest Regression')

# Bayesian Ridge Regression
axs[1, 2].scatter(x, y, label='Data', color='red')
model = BayesianRidge()
model.fit(x.reshape(-1, 1), y)
y_pred, _ = model.predict(x.reshape(-1, 1), return_std=True)
axs[1, 2].plot(x, y_pred, label='Bayesian Ridge Regression', linestyle='--')
axs[1, 2].set_title('Bayesian Ridge Regression')

# Set common labels and legends for all subplots
for ax in axs.flat:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Display the subplots
plt.savefig("plot.png")
plt.show()
