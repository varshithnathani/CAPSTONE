import random
import numpy as np

# Data: [Heart Rate, Pulse, Hemoglobin, Platelets]
data = np.array([
    [72, 75, 14.5, 250],
    [80, 78, 13.0, 300],
    [65, 70, 15.2, 220],
    [90, 85, 12.5, 280],
    [75, 77, 14.0, 350],
    [68, 72, 13.8, 275],
    [82, 80, 12.0, 290],
    [78, 79, 15.0, 260],
    [70, 74, 14.3, 230],
    [85, 82, 13.5, 310]
])

# Parameters for GA
POP_SIZE = 20
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
TOURNAMENT_SIZE = 3

# Fitness function: Minimize variance across all health metrics  =--> MIN VARIANCE ==> MORE CONSISTENT 
def fitness(individual):
    """Calculates the variance across heart rate, pulse, hemoglobin, and platelets."""
    individual_array = np.array(individual)
    # Flatten the individual to ensure each health metric is evaluated
    return np.var(individual_array, axis=0).mean()

# Create initial population
def create_individual():
    """Each individual consists of 4 rows from the dataset representing the four metrics."""
    return [data[random.randint(0, len(data) - 1)] for _ in range(4)]

def create_population(pop_size):
    """Create a population of individuals."""
    return [create_individual() for _ in range(pop_size)]

# Selection: Tournament
def select(population):
    """Select individuals using tournament selection."""
    selected = []
    for _ in range(TOURNAMENT_SIZE):
        competitors = random.sample(population, TOURNAMENT_SIZE)
        selected.append(min(competitors, key=fitness))
    return selected

# Crossover: Single point crossover
def crossover(parent1, parent2):
    """Crossover between two parents at a random point."""
    point = random.randint(1, 3)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

# Mutation: Randomly change a row of the individual
def mutate(individual):
    """Mutate an individual by randomly changing one of its rows."""
    if random.random() < MUTATION_RATE:
        index = random.randint(0, 3)
        individual[index] = data[random.randint(0, len(data) - 1)]

# Genetic Algorithm
def genetic_algorithm():
    """Main loop of the genetic algorithm."""
    population = create_population(POP_SIZE)
    for generation in range(NUM_GENERATIONS):
        # Evaluate fitness
        population = sorted(population, key=fitness)
        
        # Selection
        selected_parents = select(population)
        
        # Crossover --> single-point crossover
        """offspring1, offspring2 = crossover(parent1, parent2): 
        The crossover function is called with parent1 and parent2 as arguments. 
        This function generates two new individuals (offspring) by combining the genetic information of the parents."""
        next_population = []
        for i in range(0, len(selected_parents), 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[min(i + 1, len(selected_parents) - 1)]
            offspring1, offspring2 = crossover(parent1, parent2)
            next_population.extend([offspring1, offspring2])
        
        # Mutation
        for individual in next_population:
            mutate(individual)
        
        # Replace old population
        population = next_population
    
    # Final population
    best_solution = min(population, key=fitness)
    return best_solution

# Run GA and print the optimized solution
best_individual = genetic_algorithm()
print("Best individual (optimized set of health metrics):")
for i, entry in enumerate(best_individual):
    print(f"Entry {i+1}: Heart Rate = {entry[0]}, Pulse = {entry[1]}, Hemoglobin = {entry[2]}, Platelets = {entry[3]}")
    
print("Fitness (Variance Minimization):", fitness(best_individual))
