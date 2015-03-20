__author__ = 'tirth'

from chromosome import Chromosome
import random


class Population:
    def __init__(self, size=1000, target=42, crossover=0.7, mutation=0.001,
                 codon_length=4, gene_size=20):

        self.population = {}
        self.size = size
        self.target = target
        self.crossover_rate = crossover
        self.mutation_rate = mutation
        self.gene_info = (codon_length, gene_size)

        for i in range(self.size):
            chromosome = Chromosome(target, self.gene_info)
            self.population[chromosome] = chromosome.fitness
            if i == 0:
                self.max_value = chromosome.max_value

        self.population_fitness = sum(self.population.values()) / self.size

    def __str__(self):
        return str(list(self.population.values()))

    # reset entire population
    def extinction_event(self):
        self.__init__(self.size, self.target, self.crossover_rate,
                      self.mutation_rate, self.gene_info[0], self.gene_info[1])

    def select_random(self):
        return random.choice(list(self.population.keys()))

    def select_roulette(self):
        pick = random.uniform(0, sum(self.population.values()))
        current = 0
        for chromosome in self.population:
            current += chromosome.fitness
            if current > pick:
                return chromosome

    def mutate(self, c):
        new_c = ''

        for bit in c.dna:
            if random.random() < self.mutation_rate:
                new_c += "0" if bit == "1" else "1"
            else:
                new_c += bit

        return Chromosome(self.target, self.gene_info, new_c)

    # TODO: creating Chromosome twice, simplify?
    def cross_over(self, c1, c2):
        if random.random() < self.crossover_rate:
            start = random.randint(0, c1.length)

            temp = c1.dna[start:]
            new_c1 = Chromosome(self.target, self.gene_info,
                                c1.dna[:start] + c2.dna[start:])

            new_c2 = Chromosome(self.target, self.gene_info,
                                c2.dna[:start] + temp)

            return new_c1, new_c2
        else:
            return c1, c2

    def next_generation(self):
        new_pop = {}

        for _ in range(self.size // 2):
            uno = self.select_roulette()
            dos = self.select_roulette()

            if uno != dos:
                uno, dos = self.cross_over(self.mutate(uno), self.mutate(dos))

                new_pop[uno] = uno.fitness
                new_pop[dos] = dos.fitness

        # bring population back up
        while len(list(new_pop.keys())) < self.size:
            chromosome = Chromosome(self.target, self.gene_info)
            new_pop[chromosome] = chromosome.fitness

        self.population = new_pop
        self.population_fitness = sum(self.population.values()) / self.size