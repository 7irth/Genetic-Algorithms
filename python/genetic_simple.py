__author__ = 'tirth'

# Given the digits 0 through 9 and the operators +, -, * and /,
# find a sequence that will represent a given target number.
# The operators will be applied sequentially from left to right as you read.

from population import Population
from chromosome import Chromosome

# --------- VALUES ---------
target = 1212
population = 100
crossover_rate = 0.5
mutation_rate = 0.001
codon_length = 4
gene_size = 20
generation_reset = 200
max_generations = 100000
# --------------------------

generations = 0

print('max value: ', Chromosome(0, (4, 20)).max_value)
# target = float(input('enter target (numbers please): '))
pop_pop = Population(population, target, crossover_rate, mutation_rate,
                     codon_length, gene_size)

print('initial population fitness', pop_pop.population_fitness)
solutions = set([chromosome.equation for chromosome in pop_pop.population
                 if chromosome.fitness > 1])

while len(solutions) < 1 and generations < max_generations:
    pop_pop.extinction_event() if generations % generation_reset == 0 else \
        pop_pop.next_generation()

    generations += 1
    solutions = set([chromosome.equation for chromosome in pop_pop.population
                     if chromosome.fitness == chromosome.perfect_fit])
    print('gen', generations, 'population fitness:',
          pop_pop.population_fitness)

    # for chromosome in pop_pop.population:
    #     print(chromosome.value, end=', ')

if len(solutions) > 0:
    print('evolved {0} for {1} in {2} generations'.format(
        solutions.pop(), target, generations))
else:
    print('limit reached without success')