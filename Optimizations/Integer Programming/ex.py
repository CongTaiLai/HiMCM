"""
Objective:
Maximize 4x + 3y

Constraints:
x + 2y ≤ 6
2x + y ≤ 8
x, y are integers
"""
import pulp

# Create an instance of a minimization problem
model = pulp.LpProblem("Integer_Programming_Example", pulp.LpMaximize)

# Define integer variables
x = pulp.LpVariable("x", lowBound=0, cat='Integer')
y = pulp.LpVariable("y", lowBound=0, cat='Integer')

# Define the objective function to maximize
model += 4 * x + 3 * y, "Objective"

# Add constraints
model += x + 2 * y <= 6, "Constraint 1"
model += 2 * x + y <= 8, "Constraint 2"

# Solve the integer programming problem
model.solve()

if pulp.LpStatus[model.status] == 'Optimal':
    print("Optimal solution:")
    print("x =", x.value())
    print("y =", y.value())
    print("Optimal objective value =", pulp.value(model.objective))
else:
    print("No solution found.")
