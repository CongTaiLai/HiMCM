import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(0)

# Generate random samples from a normal (Gaussian) distribution
mu = 2  # Mean
sigma = 1  # Standard deviation
num_samples = 1000
samples = np.random.normal(mu, sigma, num_samples)

# Plot a histogram of the generated samples
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

# Plot the probability density function (PDF) of the normal distribution
x = np.linspace(-4, 4, 100)
# probability density function
pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
plt.plot(x, pdf, 'r-', lw=2)

plt.title('Normal (Gaussian) Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
