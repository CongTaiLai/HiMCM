from scipy.optimize import minimize, differential_evolution


# Define the objective function
def normal_function(x):
    return x[0] ** 4 - 3 * x[0] ** 3 + 2 * x[0] ** 2


def complicated_function(x):
    return ((x[0] + 2) ^ 2) * (x[0] - 1) * ((x[0] + 1) ^ 2) + 2


# Initial guess for the solution
initial_guess = [12.0]  # do not write [0]

# Perform the optimization
normal = minimize(normal_function, initial_guess, method='BFGS')
complicated = differential_evolution(complicated_function, [(-10, 10)])

print("Normal:")
if normal.success:
    print("Optimal solution:", normal.x)
    print("Optimal value of the objective function:", normal.fun)
else:
    print("Optimization failed:", normal.message)

print("Complicated:")
if complicated.success:
    print("Optimal solution:", complicated.x)
    print("Optimal value of the objective function:", complicated.fun)
else:
    print("Optimization failed:", complicated.message)
