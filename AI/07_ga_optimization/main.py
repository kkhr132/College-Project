import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, population_size, chromosome_length, fitness_func, mutation_rate=0.01):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.fitness_func = fitness_func
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        return [self.random_chromosome() for _ in range(self.population_size)]

    def random_chromosome(self):
        return [random.randint(0, 1) for _ in range(self.chromosome_length)]

    def fitness(self, chromosome):
        return self.fitness_func(chromosome)

    def select_parent(self):
        # Tournament selection
        tournament = random.sample(self.population, 3)
        return max(tournament, key=self.fitness)

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.chromosome_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, chromosome):
        for i in range(self.chromosome_length):
            if random.random() < self.mutation_rate:
                chromosome[i] = 1 - chromosome[i]
        return chromosome

    def evolve(self, generations):
        for generation in range(generations):
            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.select_parent()
                parent2 = self.select_parent()
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            self.population = new_population

            best_fitness = max(self.fitness(chrom) for chrom in self.population)
            print(f"Generation {generation + 1}: Best fitness = {best_fitness}")

        best_chromosome = max(self.population, key=self.fitness)
        return best_chromosome, self.fitness(best_chromosome)

# Example: Maximize the number of 1s in a binary string
def fitness_func(chromosome):
    return sum(chromosome)

if __name__ == "__main__":
    ga = GeneticAlgorithm(population_size=100, chromosome_length=20, fitness_func=fitness_func)
    best_solution, best_fitness = ga.evolve(generations=50)
    print(f"Best solution: {best_solution}")
    print(f"Best fitness: {best_fitness}")
