import random

import numpy as np

from FitnessFunctions import min_completion_latency
from Scheduler import Scheduler


class ESA_Scheduler:
    """
    A class representing the ESA algorithm for task scheduling.
    """

    def __init__(self, n_tasks, n_elephants, n_iters, cost_function):
        self.n_tasks = n_tasks
        self.n_elephants = n_elephants
        self.n_iters = n_iters
        self.population = np.array(self.initialize_population())
        self.cost_function = cost_function

    def initialize_population(self):
        population = []
        for i in range(self.n_elephants):
            schedule = list(range(self.n_tasks))
            random.shuffle(schedule)
            population.append(schedule)
        return population

    def generate_random_solution(self, n_tasks):
        schedule = list(range(n_tasks))
        random.shuffle(schedule)
        return schedule

    def run(self, tasks):
        """
        Runs the ESA
        """
        if len(tasks) < 1:
            return []

        best_schedule = self.population[0]
        best_cost = self.cost_function(best_schedule, tasks)

        for i in range(self.n_iters):
            pop_cost = np.array([self.cost_function(e, tasks) for e in self.population])
            p = pop_cost / np.sum(pop_cost)
            p = np.maximum(p, 0)
            p = p / np.sum(p)
            # choosing leader
            leader = self.population[np.random.choice(self.n_elephants, p=p)]
            leader_distance = np.sqrt(np.sum((self.population - leader) ** 2, axis=1))

            force_from_leader = np.exp(-leader_distance)
            # replace worst
            last = np.argmin(force_from_leader)
            self.population[last] = self.generate_random_solution(self.n_tasks)
            # update the best elephant (global best)
            best_schedule = self.population[
                np.argmin([self.cost_function(elephant, tasks) for elephant in self.population])]

        return best_schedule
