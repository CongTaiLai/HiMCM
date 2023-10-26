"""
Objective:
Minimize the cost function C = 5x + 7y

Constraints:
1. Production constraints:
2x + 3y ≥ 10 (You need to produce at least 10 units in total)

2. Resource constraints:
x ≤ 6 (You cannot produce more than 6 units of product X)
y ≤ 8 (You cannot produce more than 8 units of product Y)

3. Non-negativity constraints:
x ≥ 0
y ≥ 0

see: Minimize-cost.png
"""

from scipy.optimize import linprog

c = [5, 7]

A = [[-2, -3]]
b = [-10]

x_bounds = (0, 6)
y_bounds = (0, 8)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

if result.success:
    print("Optimal values:")
    print("x =", result.x[0])
    print("y =", result.x[1])
    print("Optimal objective value =", -result.fun)  # The negative sign is because linprog minimizes by default
else:
    print("No solution found.")
