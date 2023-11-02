import random
from deap import base, creator, tools, algorithms

# Create a Multi-Objective Fitness class with two objectives: maximize f1 and minimize f2
creator.create("MultiObjectiveFitness", base.Fitness, weights=(1.0, -1.0))

# Create an individual class containing two attributes
creator.create("Individual", list, fitness=creator.MultiObjectiveFitness)


# Define the optimization problem
def evaluate(individual):
    f1 = sum(individual)
    f2 = abs(len(individual) - 5)
    return f1, f2


toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selNSGA2)

# Create the population and run the NSGA-II algorithm
if __name__ == "__main__":
    population = toolbox.population(n=100)
    algorithms.eaMuPlusLambda(population, toolbox, mu=100, lambda_=100, cxpb=0.7, mutpb=0.2, ngen=50, stats=None,
                              halloffame=None, verbose=True)

    # Display the Pareto front solutions
    pareto_front = tools.sortNondominated(population, len(population), first_front_only=True)[0]
    print("Pareto Front Solutions:")
    for ind in pareto_front:
        print("Objective 1 (f1):", ind.fitness.values[0])
        print("Objective 2 (f2):", ind.fitness.values[1])
