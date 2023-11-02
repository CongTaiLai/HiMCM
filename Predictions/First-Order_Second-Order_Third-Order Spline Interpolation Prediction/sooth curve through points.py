import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Sample data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Create interpolation functions
f_linear = interp1d(x, y, kind='linear')
f_quadratic = interp1d(x, y, kind='quadratic')
f_cubic = interp1d(x, y, kind='cubic')

# Create a finer x-axis for plotting
x_new = np.linspace(0, 5, 100)

# Interpolate the y-values for the new x-axis
y_linear = f_linear(x_new)
y_quadratic = f_quadratic(x_new)
y_cubic = f_cubic(x_new)

# Plot the original data and the interpolated curves
plt.scatter(x, y, label='Data Points', color='red')
plt.plot(x_new, y_linear, label='Linear Interpolation', linestyle='--')
plt.plot(x_new, y_quadratic, label='Quadratic Interpolation', linestyle='-.')
plt.plot(x_new, y_cubic, label='Cubic Interpolation', linestyle=':')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Spline Interpolation')
plt.show()
