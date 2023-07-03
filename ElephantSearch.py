import random

from Scheduler import Scheduler


class ESA_Scheduler:
    """
    A class representing the GA algorithm for task scheduling.
    """

    def __init__(self, n_tasks, n_elephants, n_r, n_iters):
        self.n_tasks = n_tasks
        self.n_elephants = n_elephants
        self.n_r = n_r
        self.n_iters = n_iters
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for i in range(self.n_elephants):
            schedule = list(range(self.n_tasks))
            random.shuffle(schedule)
            population.append(schedule)
        return population

    def calculate_cost(self, schedule, task_list):
        return 0

    def generate_random_solution(self, n_tasks):
        schedule = list(range(n_tasks))
        random.shuffle(schedule)
        return schedule

    def mutate_schedule(self, schedule, tasks):
        if len(schedule) < 2:
            return schedule

        new_schedule = schedule.copy()
        i, j = random.sample(range(len(schedule)), 2)
        new_schedule[i], new_schedule[j] = new_schedule[j], new_schedule[i]
        return new_schedule

    def migrate_schedule(self, elephant, other, tasks):
        pass
    def run(self, tasks):
        """
        Runs the ESA
        """
        best_schedule = self.population[0]
        best_cost = self.calculate_cost(best_schedule, tasks)

        for i in range(self.n_iters):
            # Random search phase
            random_solutions = [self.generate_random_solution(self.n_tasks) for _ in range(self.n_r)]
            for solution in random_solutions:
                cost = self.calculate_cost(solution, tasks)
                if cost < best_cost:
                    best_schedule = solution
                    best_cost = cost

            # Mutation phase
            for elephant in self.population:
                new_schedule = self.mutate_schedule(elephant, tasks)
                new_cost = self.calculate_cost(new_schedule, tasks)
                if new_cost < best_cost:
                    best_schedule = new_schedule
                    best_cost = new_cost
                if new_cost < self.calculate_cost(elephant, tasks):
                    elephant = new_schedule

            # Migration phase
            for elephant in self.population:
                for other in self.population:
                    if elephant is not other:
                        new_schedule = self.migrate_schedule(elephant, other, tasks)
                        new_cost = self.calculate_cost(new_schedule, tasks)
                        if new_cost < best_cost:
                            best_schedule = new_schedule
                            best_cost = new_cost
                        if new_cost < self.calculate_cost(elephant, tasks):
                            elephant = new_schedule

        return best_schedule




