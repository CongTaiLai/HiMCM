import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the cost matrix (assignment matrix)
cost_matrix = np.array([
    [3, 2, 7],
    [2, 4, 6],
    [1, 3, 8]
])

# Find the optimal assignment using the linear_sum_assignment function
row_indices, col_indices = linear_sum_assignment(cost_matrix)

# Print the optimal assignment and total cost
print("Optimal Assignment:")
for i, j in zip(row_indices, col_indices):
    print(f"Row {i} is assigned to Column {j}")
total_cost = cost_matrix[row_indices, col_indices].sum()
print("Total Cost:", total_cost)
