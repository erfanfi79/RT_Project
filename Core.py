import random

from Dispatcher import first_fit, best_fit, worst_fit
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
        first_fit(cores, tasks, hyper_period)
    elif mapping_type == MappingType.BEST_FIT:
        best_fit(cores, tasks, hyper_period)
    elif mapping_type == MappingType.WORST_FIT:
        worst_fit(cores, tasks, hyper_period)


