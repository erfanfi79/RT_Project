import random

from Scheduler import Scheduler


class AB_Scheduler(Scheduler):
    """
    A class representing the GA algorithm for task scheduling.
    """

    def __init__(self, num_tasks, mutation_rate, crossover_rate, max_iter):

        self.pop_size = num_tasks
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.max_iter = max_iter
        super().__init__(num_tasks, mutation_rate, crossover_rate, max_iter)

    def initialize_population(self, num_tasks):
        """
        Initializes the population with random task orders.

        Args:
            num_tasks (int): Number of tasks.

        Returns:
            list: A list of task orders (chromosomes).
        """
        population = []
        for i in range(self.pop_size):
            chromosome = [j for j in range(num_tasks)]
            random.shuffle(chromosome)
            population.append(chromosome)
        return population

    def calculate_fitness(self, population, tasks):
        """
        Calculates the fitness of each chromosome in the population.

        Args:
            population (list): A list of task orders (chromosomes).
            tasks (list): A list of Task objects.

        Returns:
            list: A list of tuples containing the chromosome and its fitness.
        """
        fitness_scores = []
        for chromosome in population:
            full_time, final_time, wait_time, resp_time, slack_time = self.evaluate(chromosome, tasks)
            fitness = 1 / (1 + slack_time)
            fitness_scores.append((chromosome, fitness))
        return fitness_scores

    def evaluate(self, chromosome, tasks):
        """
        Evaluates a chromosome by simulating the execution of the tasks.

        Args:
            chromosome (list): A list representing the order of tasks to be executed.
            tasks (list): A list of Task objects.

        Returns:
            tuple: A tuple containing the full time, final time, wait time, response time, and slack time.
        """
        # TODO: Implement the task execution simulation.
        pass

    def selection(self, fitness_scores):
        """
        Selects two parent chromosomes using tournament selection.

        Args:
            fitness_scores (list): A list of tuples containing the chromosome and its fitness.

        Returns:
            tuple: A tuple containing the two parent chromosomes.
        """
        # TODO: Implement tournament selection.
        pass

    def crossover(self, parent1, parent2):
        """
        Performs crossover between two parent chromosomes.

        Args:
            parent1 (list): The first parent chromosome.
            parent2 (list): The second parent chromosome.

        Returns:
            list: The child chromosome resulting from crossover.
        """
        # TODO: Implement crossover.
        pass

    def mutate(self, chromosome):
        """
        Mutates a chromosome.

        Args:
            chromosome (list): The chromosome to mutate.

        Returns:
            list: The mutated chromosome.
        """
        # TODO: Implement mutation.
        pass

    def evolve(self, population, fitness_scores):
        """
        Evolves the population by selecting parents, performing crossover and mutation, and generating a new population.

        Args:
            population (list): A list of task orders (chromosomes).
            fitness_scores (list): A list of tuples containing the chromosome and its fitness.

        Returns:
            list: A new list of task orders (chromosomes).
        """
        # TODO: Implement evolution.
        pass

    def run(self, tasks):
        """
        Runs the GA

        """

    pass
