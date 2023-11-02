# small amount of ambiguous data

import numpy as np

# Sample data
data = np.array([30, 35, 40, 45, 50, 55, 60])


# Perform grey forecasting
def grey_forecast(data, n):
    m = len(data)
    cumulative_data = np.cumsum(data)
    cumulative_data = np.insert(cumulative_data, 0, 0)

    # Generate coefficient sequences
    a = 0.5 * (cumulative_data[1:m + 1] + cumulative_data[0:m])
    b = -1 * data

    # Calculate the grey forecast
    x0 = data[-1]
    forecast = np.zeros(n)
    for i in range(n):
        forecast[i] = (x0 - b[m - 1] / a[m - 1]) * np.exp(-a[m - 1] * i) + b[m - 1] / a[m - 1]

    return forecast


# Number of future periods to forecast
n_periods = 3
forecasted_data = grey_forecast(data, n_periods)
print("Original Data:", data)
print("Grey Forecast for the next", n_periods, "periods:", forecasted_data)
