import random
from Task import Task
from enum import Enum


class MappingType(Enum):
    FIRST_FIT = 1
    WORST_FIT = 2
    BEST_FIT = 3


class Core:
    def __init__(self, core_id):
        self.core_id = core_id
        self.assigned_tasks = []
        self.utilization = 1

    def assign_task(self, task):
        self.assigned_tasks.append(task)
        self.utilization -= (task.execution_time / (task.deadline - task.arrival_time))

    def calculate_free_time(self, current_time, end_time):
        overlapping_tasks = [o_task for o_task in self.assigned_tasks if o_task.deadline > current_time]
        busy_time = sum([min(o_task.execution_time, o_task.deadline - current_time) for o_task in overlapping_tasks])
        return end_time - current_time - busy_time

def assign_tasks(cores, tasks, hyper_period, mapping_type):
    if mapping_type == MappingType.FIRST_FIT:
        assign_by_first_fit(cores, tasks, hyper_period)
    elif mapping_type == MappingType.BEST_FIT:
        assign_by_best_fit(cores, tasks, hyper_period)
    elif mapping_type == MappingType.WORST_FIT:
        assign_by_worst_fit(cores, tasks, hyper_period)


def assign_by_first_fit(cores, tasks, hyper_period):
    # Assign tasks to cores using the first fit algorithm
    for task in tasks:
        assigned = False
        for core in cores:
            if core.calculate_free_time(task.arrival_time, hyper_period) >= task.execution_time:
                core.assign_task(task)
                assigned = True
                break
        if not assigned:
            print("No available core for task:", task.id)


def assign_by_best_fit(cores, tasks, hyper_period):
    # Assign tasks to cores using the best fit algorithm
    for task in tasks:
        utilizations = [(core, core.calculate_free_time(task.arrival_time, hyper_period)) for core in cores]

        assigned = False
        for core, free_time in sorted(utilizations, key=lambda x: x[1]):
            if free_time >= task.execution_time:
                core.assign_task(task)
                assigned = True
                break

        if not assigned:
            print("No available core for task:", task.id)


def assign_by_worst_fit(cores, tasks, hyper_period):
    # Assign tasks to cores using the worst fit algorithm
    for task in tasks:
        utilizations = [(core, core.calculate_free_time(task.arrival_time, hyper_period)) for core in cores]

        for core, free_time in sorted(utilizations, key=lambda x: x[1], reverse=True):
            if free_time >= task.execution_time:
                core.assign_task(task)
                break
            print("No available core for task:", task.id)
            break