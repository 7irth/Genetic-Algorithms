__author__ = 'tirth'

from chromosome import Chromosome
import random


class Population:
    def __init__(self, size=1000, target=42):
        self.population = {}
        self.size = size
        self.target = target
        self.crossover_rate = 0.7
        self.mutation_rate = 0.001

        for _ in range(self.size):
            chromosome = Chromosome()
            chromosome.set_fitness(target)
            self.population[chromosome.fitness] = chromosome

    def __str__(self):
        return str(list(self.population.keys()))

    def select_one(self):
        return self.population.get(random.choice(list(self.population.keys())))
