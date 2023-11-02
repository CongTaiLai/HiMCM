import numpy as np

# Sample sequence of states
states_sequence = ["Sunny", "Sunny", "Cloudy", "Rainy", "Cloudy", "Sunny", "Sunny"]

# Define the states
states = ["Sunny", "Cloudy", "Rainy"]

# Initialize the transition matrix with zeros
transition_matrix = np.zeros((len(states), len(states)))

# Count transitions from the data
for i in range(1, len(states_sequence)):
    prev_state = states_sequence[i - 1]
    current_state = states_sequence[i]
    prev_state_index = states.index(prev_state)
    current_state_index = states.index(current_state)
    transition_matrix[prev_state_index, current_state_index] += 1

# Normalize the transition matrix to get probabilities
transition_matrix = transition_matrix / transition_matrix.sum(axis=1)[:, np.newaxis]

# Print the estimated transition matrix
print("Estimated Transition Matrix:")
print(transition_matrix)
