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
            chromosome = Chromosome(target)
            self.population[chromosome] = chromosome.fitness

        self.population_fitness = sum(self.population.values()) / self.size

    def __str__(self):
        return str(list(self.population.values()))

    def select_random(self):
        return random.choice(list(self.population.keys()))

    def select_roulette(self):
        pick = random.uniform(0, sum(self.population.values()))
        current = 0
        for chromosome in self.population:
            current += chromosome.fitness
            if current > pick:
                return chromosome

    def new_population(self):
        new_pop = {}
        for _ in range(self.size):
            a = self.select_roulette()
            new_pop[a] = a.fitness

        print(self.population.values())
        print(new_pop.values())

        print('old fitness', self.population_fitness)
        print('new fitness', sum(new_pop.values()) / len(list(new_pop.keys())))