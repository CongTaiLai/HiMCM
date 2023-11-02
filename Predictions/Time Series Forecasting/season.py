import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Create a simple time series dataset
data = {'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'value': [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]}
# data = {'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
#         'value': [10, 11, 14, 17, 19, 20, 25, 28, 26, 28]}

df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Visualize the time series data
plt.figure(figsize=(10, 6))
plt.plot(df, marker='o')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Data')
plt.show()

# Perform time series forecasting using Holt-Winters method
model = ExponentialSmoothing(df['value'], trend='add', seasonal='add', seasonal_periods=3)
model_fit = model.fit(optimized=True)
forecast = model_fit.forecast(steps=3)

# Visualize the original data and the forecast
plt.figure(figsize=(10, 6))
plt.plot(df, marker='o', label='Original Data')
plt.plot(pd.date_range(start='2023-01-11', periods=3, freq='D'), forecast, marker='o', label='Forecast', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Forecasting')
plt.legend()
plt.show()

print("Forecasted values for the next 3 periods:")
print(forecast)
