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
import pulp

model = pulp.LpProblem("Linear_Programming_Example", pulp.LpMaximize)

x = pulp.LpVariable("x", lowBound=0, cat="Linear")
y = pulp.LpVariable("y", lowBound=0, cat="Linear")

model += 3 * x + 2 * y, "Objective"
model += x + y <= 4, "Constraint 1"
model += 2 * x + y <= 5, "Constraint 2"

model.solve()
if pulp.LpStatus[model.status] == 'Optimal':
    print("Optimal values:")
    print("x =", x.value())
    print("y =", y.value())
    print("Optimal objective value =",
          pulp.value(model.objective))  # The negative sign is because linprog minimizes by default
else:
    print("No solution found.")
