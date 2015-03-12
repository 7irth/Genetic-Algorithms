__author__ = 'tirth'

# Given the digits 0 through 9 and the operators +, -, * and /,
# find a sequence that will represent a given target number.
# The operators will be applied sequentially from left to right as you read.

from random import random


class Chromosome:
    def __init__(self):
        self.genes = ''
        self.codon_size = 4
        self.number_of_genes = 9
        self.length = self.codon_size * self.number_of_genes

        while len(self.genes) < self.length:
            self.genes += ('0' if random() < 0.5 else '1')

        print(self.genes)

        self.value = self.get_value()

    def convert_genes(self):
        converted = ''

        for i in range(self.codon_size, self.length + 1, self.codon_size):
            gene_value = int(self.genes[i - self.codon_size:i], 2)

            if gene_value == 10:
                converted += '+'
            elif gene_value == 11:
                converted += '-'
            elif gene_value == 12:
                converted += '*'
            elif gene_value == 13:
                converted += '/'
            elif gene_value == 14 or gene_value == 15:
                converted += ''
            else:
                converted += str(gene_value)

        return converted

    def cleaned_up(self):
        raw = self.convert_genes()
        print(raw)
        equation = ""
        last = 0
        started = False

        for element in range(len(raw)):
            current = raw[element]

            if not started and current.isdigit():
                last = element
                equation += current
                started = True

            if started:
                # operation
                if raw[last].isdigit() and not current.isdigit():
                    last = element
                    equation += current

                # number
                elif not raw[last].isdigit() and current.isdigit():
                    last = element
                    equation += current

        # TODO: account for edge equation cases
        return equation[:-1] if not equation[-1].isdigit() else equation

    # sequential evaluation
    def get_value(self):
        equation = self.cleaned_up()
        print(equation)
        value = equation[0]

        for i in range(1, len(equation), 2):
            value = eval(str(value) + equation[i] + equation[i + 1])

        return value


if __name__ == '__main__':
    test_chromosome = Chromosome()
    print(test_chromosome.value)
