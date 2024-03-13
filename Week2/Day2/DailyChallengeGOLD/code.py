import random


class Gene:
    def __init__(self, value=random.randint(0, 1)):
        self.value = value

    def mutate(self):
        self.value = 1 - self.value


class Chromosome:
    def __init__(self, genes=(random.randint(0, 1) for _ in range(10))):
        self.genes = genes

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome([Gene(random.randint(0, 1)) for _ in range(10)]) for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    # def all_ones(self):
    #     for chromosome in self.chromosomes:
    #         for gene in chromosome.genes:
    #             if gene.value != 1:
    #                 return False
    #     return True
    #

    # Changed method all_ones to search all 1s in one chromosome, not in whole DNA
    def all_ones(self):
        for chromosome in self.chromosomes:
            count = 0
            for gene in chromosome.genes:
                if gene.value == 1:
                    count += 1
                else:
                    count = 0
            if count == 10:
                return True
            else:
                return False


class Organism:
    def __init__(self, environment):
        self.dna = DNA()
        self.environment = environment

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def __str__(self):
        return f"Organism with environment: {self.environment}"


def main():
    generations = 0
    organism = Organism(0.1)

    while True:
        generations += 1
        organism.mutate()
        if organism.dna.all_ones():
            print(f"{organism} found target DNA after {generations} generations.")
            return False


main()
