"""
Objective:
Maximize 3x + 2y

Constraints:
x ≥ 0
y ≥ 0
x + y ≤ 4
2x + y ≤ 5

see: Maximize.png
"""

from scipy.optimize import linprog

# Coefficients of the objective function to be maximized
c = [-3, -2] # positive or negative depends on objective is max or min

# Coefficients of the inequality constraints (Ax <= b)
A = [[1, 1], [2, 1]]
b = [4, 5]

# Bounds for variables (x and y)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

if result.success:
    print("Optimal values:")
    print("x =", result.x[0])
    print("y =", result.x[1])
    print("Optimal objective value =", -result.fun)  # The negative sign is because linprog minimizes by default
else:
    print("No solution found.")
