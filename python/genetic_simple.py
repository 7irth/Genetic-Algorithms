__author__ = 'tirth'

# Given the digits 0 through 9 and the operators +, -, * and /,
# find a sequence that will represent a given target number.
# The operators will be applied sequentially from left to right as you read.

from population import Population

# --------- VALUES ---------
target = 42
generations = 5
population = 2000
crossover_rate = 0.7
mutation_rate = 0.001
# --------------------------

pop_pop = Population(population, target, crossover_rate, mutation_rate)

print('initial population fitness', pop_pop.population_fitness)
solutions = [chromosome.equation for chromosome in pop_pop.population
             if chromosome.fitness > 1]
print('initial things for', target, set(solutions), '\n')

for _ in range(generations):
    pop_pop.next_generation()

print('fitness after', generations, 'generations', pop_pop.population_fitness)
solutions = [chromosome.equation for chromosome in pop_pop.population
             if chromosome.fitness > 1]
print('evolved things for', target, set(solutions))