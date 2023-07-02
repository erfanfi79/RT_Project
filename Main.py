import enum

from Task import Task
from ElephantSearch import ESA_Scheduler
from ArtificialBeeColony import ABC_Scheduler
from Core import Core, assign_tasks, MappingType
from task_generation import generate_tasks_instances


class CoreAssignType(enum.Enum):
    WF = "worst fit"
    BF = "best fit"
    FT = "first fit"


class SchedulingType(enum.Enum):
    ABC = "Artificial bee colony"
    ESA = "Elephant search algorithm"


def make_multicore_scheduling(num_cores, mapping_type, u_total, scheduling_type):
    cores = [Core(i) for i in range(num_cores)]
    task_instances, hyper_period = generate_tasks_instances(2, u_total=u_total)
    assign_tasks(cores, task_instances, hyper_period, mapping_type)
    if scheduling_type == SchedulingType.ABC:
        ABC = ABC_Scheduler(len(task_instances), 10, 10, 10, 10)
        ABC.run(task_instances)


if __name__ == '__main__':
    make_multicore_scheduling(5, MappingType.FIRST_FIT, 1, SchedulingType.ABC)
