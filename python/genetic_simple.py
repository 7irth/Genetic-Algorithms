__author__ = 'tirth'

# Given the digits 0 through 9 and the operators +, -, * and /,
# find a sequence that will represent a given target number.
# The operators will be applied sequentially from left to right as you read.

from chromosome import Chromosome

population = {}
population_size = 100
target = 42

for i in range(population_size):
    chromosome = Chromosome()
    chromosome.set_fitness(target)
    population[chromosome.dna] = chromosome

print(population)