import enum

from Task import Task
from ElephantSearch import ESA_Scheduler
from ArtificialBeeColony import ABC_Scheduler
from Core import Core
from task_generation import generate_tasks_instances


class CoreAssignType(enum.Enum):
    WF = "worst fit"
    BF = "best fit"
    FT = "first fit"


class SchedulingType(enum.Enum):
    ABC = "Artificial bee colony"
    ESA = "Elephant search algorithm"


def assign_to_cores(cores, task_instances, assign_type):
    pass


def make_multicore_scheduling(num_cores, core_type, u_total, scheduling_type):
    cores = [Core(i) for i in range(num_cores)]
    task_instances, hyper_period = generate_tasks_instances(2, u_total=u_total)
    assign_to_cores(cores, task_instances, core_type)
    if scheduling_type == SchedulingType.ABC:
        ABC = ABC_Scheduler()
        ABC.run()
