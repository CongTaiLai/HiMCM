import pulp

# Define the job shop scheduling instance
num_jobs = 3
num_machines = 3

# Processing times (job x machine)
processing_times = [
    [2, 1, 3],
    [4, 3, 2],
    [3, 2, 1]
]  # each job represents each list, each var in list represent machine

# Create a PuLP problem
problem = pulp.LpProblem("Job_Shop_Scheduling", pulp.LpMinimize)

# Define decision variables
x = [[[pulp.LpVariable(f'x_{i}_{j}_{k}', cat=pulp.LpBinary) for k in range(num_machines)] for j in range(num_jobs)] for i in range(num_jobs)]

# Define the objective function (minimize makespan)
problem += pulp.lpSum((k + 1) * x[i][j][k] for i in range(num_jobs) for j in range(num_jobs) for k in range(num_machines))

# Define constraints
# Each job must be processed on each machine exactly once
for i in range(num_jobs):
    for k in range(num_machines):
        problem += pulp.lpSum(x[i][j][k] for j in range(num_jobs)) == 1
for j in range(num_jobs):
    for k in range(num_machines):
        problem += pulp.lpSum(x[i][j][k] for i in range(num_jobs)) == 1

# Job precedences (jobs are processed in a specific order)
problem += x[0][1][0] == 1
problem += x[1][2][0] == 1

# Solve the problem
problem.solve()

# Print the schedule
schedule = [[[-1 for _ in range(num_machines)] for _ in range(num_jobs)] for _ in range(num_jobs)]
for var in problem.variables():
    if var.varValue == 1:
        i, j, k = map(int, var.name.split('_')[1:])
        schedule[i][j][k] = var.name

# Print the schedule
print("Schedule:")
for i in range(num_jobs):
    for j in range(num_jobs):
        print(f"Job {i} -> Job {j}: ", end='')
        for k in range(num_machines):
            if schedule[i][j][k] != -1:
                print(f"Machine {k} ", end='')
        print()
