__author__ = 'tirth'

from random import random


class Chromosome:
    def __init__(self, dna=None):
        self.codon_size = 4
        self.number_of_genes = 9
        self.length = self.codon_size * self.number_of_genes

        if dna:
            self.dna = dna
        else:
            self.dna = ''
            while len(self.dna) < self.length:
                self.dna += ('0' if random() < 0.5 else '1')

        self.value = float(self.evaluate())
        self.fitness = None

    # dna to genes (numbers and operators)
    def transcription(self):
        genes = ''

        # decoding
        for i in range(self.codon_size, self.length + 1, self.codon_size):
            gene = int(self.dna[i - self.codon_size:i], 2)

            if gene == 10:
                genes += '+'
            elif gene == 11:
                genes += '-'
            elif gene == 12:
                genes += '*'
            elif gene == 13:
                genes += '/'
            elif gene == 14 or gene == 15:
                genes += ''
            else:
                genes += str(gene)

        return genes

    # genes to protein (equation)
    def translation(self):
        genes = self.transcription()
        equation = ""
        at = 0
        started = False

        for i in range(len(genes)):
            current = genes[i]

            if not started and current.isdigit():
                at = i
                equation += current
                started = True

            if started and (genes[at].isdigit() and not current.isdigit()) \
                    or (not genes[at].isdigit() and current.isdigit()):
                at = i
                equation += current

        # account for edge equation cases
        equation = '0' if not started else equation.replace('/0', '')

        return equation[:-1] if not equation[-1].isdigit() else equation

    # sequential evaluation
    def evaluate(self):
        equation = self.translation()
        value = equation[0]

        for i in range(1, len(equation), 2):
            value = eval(str(value) + equation[i] + equation[i + 1])

        return value

    def set_fitness(self, target):
        if self.value == target:
            self.fitness = 2
        else:
            self.fitness = abs(1 / (target - self.value))