__author__ = 'tirth'

# Given the digits 0 through 9 and the operators +, -, * and /,
# find a sequence that will represent a given target number.
# The operators will be applied sequentially from left to right as you read.

from population import Population
from chromosome import Chromosome

# --------- VALUES ---------
target = 120
population = 1000
crossover_rate = 0.7
mutation_rate = 0.001
# --------------------------

generations = 0

print('max value: ', Chromosome(0).max_value)
# target = float(input('enter target (ints please): '))
pop_pop = Population(population, target, crossover_rate, mutation_rate)

print('initial population fitness', pop_pop.population_fitness)
solutions = set([chromosome.equation for chromosome in pop_pop.population
                 if chromosome.fitness > 1])

while len(solutions) < 1:
    pop_pop.next_generation()
    generations += 1
    solutions = set([chromosome.equation for chromosome in pop_pop.population
                     if chromosome.fitness > 1])
    print('current population fitness', pop_pop.population_fitness,
          generations)

print('evolved {0} for {1} in {2} generations'.format(
    solutions.pop(), target, generations))