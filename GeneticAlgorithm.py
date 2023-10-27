from random import choices, randint, randrange, random, sample
from typing import List, Optional, Callable, Tuple

#=========================================================================
#define GA objects
#=========================================================================
chromosome = List[int]
Population = List[chromosome]

#=========================================================================
#define processes in a GA
#=========================================================================
FitnessFunc = Callable[[chromosome], int] #fitness evaluation function
#PrinterFunc = Callable[[Population, int, FitnessFunc], None] # print individual and associated fitness

class GeneticAlgorithm:
    def __init__(self, generation_limit: int = 100,):
        self.populateFunc = self.generate_population
        self.fitness_func = FitnessFunc
        self.generation_limit = generation_limit
        self.generation = 0
        self.population = []

    def generate_chromosome(self, length: int) -> chromosome:
        return choices([0, 1], k=length)

    def generate_population(self, size: int, chromosome_length: int) -> Population:
        """
        generate individuals based size given
        :param tab: chromosome size and number of chromosomes  
        :return: initial population
        """
        return [self.generate_chromosome(chromosome_length) for _ in range(size)]

    def one_point_crossover(self, a: chromosome, b: chromosome) -> Tuple[chromosome, chromosome]:
        """
        Perform one-point crossover to generate new individuals based on chromosome size.
    
        :param a: The first parent chromosome.
        :param b: The second parent chromosome.
        :return: A tuple containing two new chromosomes resulting from crossover.
        """

        if len(a) != len(b):
            raise ValueError("Genomes a and b must be of the same length")

        length = len(a)
        if length < 2:
            return a, b

        #generate random point
        p = randint(1, length - 1)

        #copy genetic material
        child1 = a[:p] + b[p:]
        child2 = b[:p] + a[p:]

        return child1, child2

    

    def uniform_mutation(self, genome: chromosome, mutation_probability: float) -> chromosome:
        """
        Apply uniform mutation to a given genome based on a specified mutation probability.
    
        :param genome: The genome (chromosome) to mutate.
        :param mutation_probability: The probability of mutation for each gene (0.0 to 1.0).
        :return: The mutated genome.
        """

        mutated_genome = []

        for gene in genome:
            if random() < mutation_probability:
                # If mutation occurs, replace the gene with a random value (0 or 1)
                mutated_gene = randint(0, 1)
            else:
                mutated_gene = gene

            mutated_genome.append(mutated_gene)

        return mutated_genome


    def elitism_selection(self, population: Population, fitness_func: FitnessFunc) -> Population:
        """
        Select a pair of individuals from the population using weighted random sampling based on fitness.

        :param population: The population of individuals.
        :param fitness_func: A function to evaluate the fitness of an individual.
        :return: A pair of selected individuals.
        """
        return sample(
            population=self.generate_weighted_distribution(population, fitness_func),
            k=2,
        )

    def population_fitness(self, population: Population, fitness_func: FitnessFunc) -> int:
        """
        Calculate the total fitness of a population by summing the fitness values of its individuals.

        :param population: The population of individuals.
        :param fitness_func: A function to evaluate the fitness of an individual.
        :return: The total fitness of the population.
        """
        return sum(map(fitness_func, population))
    
    def generate_weighted_distribution(self, population: Population, fitness_func: FitnessFunc) -> Population:
        weighted_population = []
    
        total_fitness = sum(fitness_func(individual) for individual in population)
    
        for individual in population:
            fitness = fitness_func(individual)
            # Calculate the weight for each individual based on their fitness
            weight = fitness / total_fitness
            # Append the individual multiple times based on its weight
            weighted_population.extend([individual] * int(weight * 100))
    
        return weighted_population


    