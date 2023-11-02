import random
import pulp
import matplotlib.pyplot as plt

# Define the number of customers and vehicles
num_customers = 10
num_vehicles = 3

# Set random seed for reproducibility
random.seed(0)

# Generate random customer demands and locations
customer_demands = [random.randint(1, 10) for _ in range(num_customers)]
customer_locations = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_customers)]

# Generate random vehicle capacities and locations
vehicle_capacities = [20 for _ in range(num_vehicles)]
vehicle_locations = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_vehicles)]

# Create a PuLP problem
problem = pulp.LpProblem("Vehicle_Routing_Problem", pulp.LpMinimize)

# Define decision variables
x = [[pulp.LpVariable(f'x_{i}_{j}', cat=pulp.LpBinary) for j in range(num_customers)] for i in range(num_vehicles)]

# Define the objective function
problem += pulp.lpSum(x[i][j] for i in range(num_vehicles) for j in range(num_customers))

# Define constraints
for j in range(num_customers):
    problem += pulp.lpSum(x[i][j] for i in range(num_vehicles)) == 1  # Each customer is visited exactly once

for i in range(num_vehicles):
    problem += pulp.lpSum(x[i][j] * customer_demands[j] for j in range(num_customers)) <= vehicle_capacities[i]  # Vehicle capacity

# Solve the problem
problem.solve()

# Extract the solution
routes = []
for i in range(num_vehicles):
    route = [j for j in range(num_customers) if pulp.value(x[i][j]) == 1]
    if route:
        routes.append(route)

# Print the routes
for i, route in enumerate(routes):
    print(f"Vehicle {i + 1} visits customers: {route}")

# Print the objective value
print(f"Total Distance Traveled: {pulp.value(problem.objective):.2f}")

# Plot the VRP routes
plt.figure(figsize=(8, 8))
plt.scatter([loc[0] for loc in customer_locations], [loc[1] for loc in customer_locations], c='b', marker='o', label='Customers')
plt.scatter([loc[0] for loc in vehicle_locations], [loc[1] for loc in vehicle_locations], c='r', marker='s', label='Vehicles')

for i, route in enumerate(routes):
    route_locs = [customer_locations[j] for j in route]
    route_locs.insert(0, vehicle_locations[i])
    route_locs.append(vehicle_locations[i])
    xs, ys = zip(*route_locs)
    plt.plot(xs, ys, '->', label=f'Vehicle {i + 1} Route')

plt.title('Vehicle Routing Problem Solution')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.show()