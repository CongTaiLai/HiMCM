import pulp


def multi_dimensional_knapsack():
    # Create a PuLP problem
    problem = pulp.LpProblem("Multi_Dimensional_Knapsack", pulp.LpMaximize)

    # Define the items and their attributes
    items = range(20)
    values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17]
    weights_dim1 = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 95]
    weights_dim2 = [0, 2, 0, 0, 0, 3, 3, 1, 5, 0, 5, 2, 3, 0, 1, 1, 3, 0, 1, 5]

    # Define the decision variables
    x = pulp.LpVariable.dicts("item", items, 0, 1, pulp.LpBinary)

    # Define the objective function
    problem += pulp.lpSum(x[i] * values[i] for i in items), "Total Value"

    # Define the capacity constraints for each dimension
    for d in range(2):
        problem += pulp.lpSum(x[i] * weights_dim1[i] for i in items) <= 850, f"Dimension 1 Capacity {d}"
        problem += pulp.lpSum(x[i] * weights_dim2[i] for i in items) <= 60, f"Dimension 2 Capacity {d}"

    # Solve the problem
    problem.solve()

    # Print the results
    print("Status:", pulp.LpStatus[problem.status])
    print("Optimal Objective Value:", pulp.value(problem.objective))
    selected_items = [i for i in items if x[i].value() == 1]
    print("Selected Items:", selected_items)


if __name__ == "__main__":
    multi_dimensional_knapsack()
