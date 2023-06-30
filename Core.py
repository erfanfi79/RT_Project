import random
from Task import Task


class Core:
    def __init__(self, core_id):
        self.core_id = core_id
        self.assigned_tasks = []

    def assign_task(self, task):
        self.assigned_tasks.append(task)

    def calculate_free_time(self, current_time, end_time):
        overlapping_tasks = [o_task for o_task in self.assigned_tasks if o_task.deadline > current_time]
        busy_time = sum([min(o_task.execution_time, o_task.deadline - current_time) for o_task in overlapping_tasks])
        return end_time - current_time - busy_time

    def schedule_tasks(self):
        # Artificial Bee Colony (ABC) algorithm implementation
        # Modify this method according to your specific scheduling requirements

        # Initialize the ABC algorithm parameters
        population_size = 10
        limit = 10
        num_iterations = 100

        # Initialize the population of solutions (core assignments)
        solutions = []
        for _ in range(population_size):
            solution = [random.choice(self.assigned_tasks) for _ in range(len(self.assigned_tasks))]
            solutions.append(solution)

        # Perform the ABC algorithm iterations
        for iteration in range(num_iterations):
            for i, solution in enumerate(solutions):
                # Employed bee phase
                neighbor_solution = self.local_search(solution)
                if self.calculate_fitness(neighbor_solution) < self.calculate_fitness(solution):
                    solutions[i] = neighbor_solution
                else:
                    # Onlooker bee phase
                    neighbor_index = random.randint(0, population_size - 1)
                    neighbor_solution = self.local_search(solutions[neighbor_index])
                    if self.calculate_fitness(neighbor_solution) < self.calculate_fitness(solution):
                        solutions[i] = neighbor_solution

            # Scout bee phase
            for i, solution in enumerate(solutions):
                if self.calculate_fitness(solution) > limit:
                    solutions[i] = self.initialize_random_solution()

        # Select the best solution
        best_solution = min(solutions, key=self.calculate_fitness)

        # Assign the tasks to the core based on the best solution
        self.assigned_tasks = best_solution

    def local_search(self, solution):
        # Modify this method to perform local search around the current solution
        # Return the improved solution after the local search
        return solution

    def calculate_fitness(self, solution):
        # Modify this method to calculate the fitness of a solution based on your scheduling criteria
        return sum(task.execution_time for task in solution)

    def initialize_random_solution(self):
        # Randomly initialize a solution (core assignment)
        return random.sample(self.assigned_tasks, len(self.assigned_tasks))


def main():
    # Example usage
    tasks = [
        Task(1, 0, 10, 5),
        Task(2, 2, 8, 3),
        Task(3, 4, 12, 7),
        Task(4, 1, 9, 4)
    ]

    cores = [
        Core(1),
        Core(2),
        Core(3)
    ]

    total_deadline = max([task.deadline for task in tasks])

    # Assign tasks to cores using the first fit algorithm
    for task in tasks:
        assigned = False
        for core in cores:
            if core.calculate_free_time(task.arrival_time, total_deadline) >= task.execution_time:
                core.assign_task(task)
                assigned = True
                break
        if not assigned:
            print("No available core for task:", task.id)

    # Schedule tasks on each core using the Artificial Bee Colony algorithm
    for core in cores:
        core.schedule_tasks()

    # Print the assignments for each core
    for core in cores:
        print("Core", core.core_id, "assigned tasks:", [task.id for task in core.assigned_tasks])


if __name__ == '__main__':
    main()
