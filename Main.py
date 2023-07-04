import enum

from ArtificialBeeColony import ABC_Scheduler
from Core import Core, assign_tasks, MappingType
from Output import generate_json_output
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
    task_instances, hyper_period = generate_tasks_instances(n=2, u_total=u_total)
    assign_tasks(cores, task_instances, hyper_period, mapping_type)
    schedules = []
    if scheduling_type == SchedulingType.ABC:
        for core in cores:
            ABC = ABC_Scheduler(len(core.assigned_tasks), 30, 30, 30, 40)
            schedule = ABC.run(core.assigned_tasks)
            schedules.append(schedule)

    for idx, schedule in enumerate(schedules):
        print([cores[idx].assigned_tasks[task_idx].id for task_idx in schedule])

    for core_idx, schedule in enumerate(schedules):
        current_time = 0
        for task_index in schedule:
            task = cores[core_idx].assigned_tasks[task_index]
            task.start_time = current_time
            task.finish_time = current_time + task.execution_time
            task.waiting_time = task.finish_time - task.execution_time - task.arrival_time
            task.response_time = task.finish_time - task.arrival_time
            task.slack_time = task.finish_time - task.execution_time - task.arrival_time

            current_time += task.execution_time

            if task.finish_time > task.deadline:
                print(f"task {task_index} deadline missed. finish_time: {task.finish_time}, deadline: {task.deadline}")

    output = generate_json_output(cores=cores, algorithm_convergence_time=0)
    write_output_to_file("./output.json")


def write_output_to_file(filepath):
    with open(filepath, 'w') as json_file:
        json_file.write(filepath)


if __name__ == '__main__':
    make_multicore_scheduling(2, MappingType.WORST_FIT, 1, SchedulingType.ABC)
