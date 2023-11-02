# making guesses about what will happen next based on what's happening now
import numpy as np

# Define the states (e.g., Sunny, Cloudy, Rainy)
states = ["Sunny", "Cloudy", "Rainy"]

# Define the transition probabilities for a first-order Markov chain
# The rows represent the current state, and the columns represent the next state
transition_matrix = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.1, 0.3, 0.6]
])

# Initialize the current state
current_state = "Sunny"

# Perform a Markov prediction for a certain number of days
n_days = 7
predicted_weather = [current_state]

for _ in range(n_days):
    current_state_index = states.index(current_state)
    next_state_index = np.random.choice(len(states), p=transition_matrix[current_state_index])
    current_state = states[next_state_index]
    predicted_weather.append(current_state)

# Print the predicted weather for the specified number of days
print("Predicted Weather for the Next", n_days, "Days:")
print(predicted_weather[1:])
