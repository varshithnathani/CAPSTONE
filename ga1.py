# -*- coding: utf-8 -*-
"""GA1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J6TOvu9xt2L4b1mD0F94zi74ob9NWutc
"""



import random

# Define the distances of the 5 sensors
sensor_distances = [74.33, 120, 76.16, 146.41, 146.09]

# Parameters for the genetic algorithm
population_size = 10
generations = 100
mutation_rate = 0.3
tournament_size = 3

# Function to calculate the fitness (lower is better)
def fitness(solution):
    # The fitness is the sum of sensor distances (minimizing total latency)
    return sum(solution)

# Generate a random individual (a random permutation of sensors)
def generate_individual():
    return random.sample(sensor_distances, len(sensor_distances))

# Create the initial population
def generate_population(size):
    return [generate_individual() for _ in range(size)]

# Tournament selection: select the best individual from a random subset
def tournament_selection(population):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=fitness)
    return tournament[0]

# Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    child2 = parent2[:point] + [gene for gene in parent1 if gene not in parent2[:point]]
    return child1, child2

# Mutation: swap two random genes (sensor distances)
def mutate(individual):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Genetic Algorithm
def genetic_algorithm():
    # Step 1: Initialize population
    population = generate_population(population_size)

    for generation in range(generations):
        new_population = []

        # Step 2: Selection, Crossover, and Mutation
        while len(new_population) < population_size:
            # Selection
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            mutate(child1)
            mutate(child2)

            # Add children to the new population
            new_population.append(child1)
            new_population.append(child2)

        # Replace old population with new population
        population = new_population

        # Step 3: Sort by fitness (to keep track of the best solution)
        population.sort(key=fitness)

        # Print the best solution of the current generation
        print(f"Generation {generation + 1}, Best Solution: {population[0]}, Fitness: {fitness(population[0])}")

    # Step 4: Return the best solution found
    return population[0]

# Run the genetic algorithm
best_solution = genetic_algorithm()
print(f"Optimized Sensor Placement: {best_solution}, Latency: {fitness(best_solution)}")