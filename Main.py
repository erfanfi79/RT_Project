import enum
import json

from ArtificialBeeColony import ABC_Scheduler
from Core import Core, assign_tasks, MappingType
from ElephantSearch import ESA_Scheduler
from FitnessFunctions import *
from Output import generate_json_output
from task_generation import read_task_instances_from_file, create_tasks


class SchedulingType(enum.Enum):
    ABC = "ABC"
    ESA = "ESA"


def make_multicore_scheduling(num_cores, mapping_type, u_total, scheduling_type, fitness_function):
    cores = [Core(i) for i in range(num_cores)]
    task_instances, hyper_period = read_task_instances_from_file('./task_instances_u_' + str(u_total) + '.json')
    assign_tasks(cores, task_instances, hyper_period, mapping_type)
    schedules = []
    if scheduling_type == SchedulingType.ABC:
        for core in cores:
            ABC = ABC_Scheduler(len(core.assigned_tasks), 30, 30, 30, 30, fitness_function)
            schedule = ABC.run(core.assigned_tasks)
            schedules.append(schedule)
    else:
        for core in cores:
            ESA = ESA_Scheduler(len(core.assigned_tasks), 30, 30, fitness_function)
            schedule = ESA.run(core.assigned_tasks)
            schedules.append(schedule)

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

            # if task.finish_time > task.deadline:
            #     print(f"task {task_index} deadline missed. finish_time: {task.finish_time}, deadline: {task.deadline}")

    result = generate_json_output(cores=cores, algorithm_convergence_time=0)
    return result


def write_output_to_file(filepath, result):
    with open(filepath, 'w') as json_file:
        json_file.write(result)


if __name__ == '__main__':
    task_num = 10

    fitness_functions = [min_completion_latency, min_response_wait, min_wait_latency, min_response_latency,
                         min_completion_response, min_completion_sumOfSlack, min_completion_latency_response,
                         min_completion_sumOfSlack_response]
    fitness_functions_name = ['min_completion_latency', 'min_response_wait', 'min_wait_latency', 'min_response_latency',
                              'min_completion_response', 'min_completion_sumOfSlack', 'min_completion_latency_response',
                              'min_completion_sumOfSlack_response']
    multicore = [1, 2, 4, 8, 16, 32]
    mapping_type = [MappingType.FIRST_FIT, MappingType.WORST_FIT, MappingType.BEST_FIT]
    utilization = [0.1, 0.3, 0.5, 0.7, 0.9, 1]
    algorithm = [SchedulingType.ABC, SchedulingType.ESA]
    for u in utilization:
        output = []
        create_tasks(task_num=task_num, u_total=u, filepath="task_instances_u_" + str(u) + ".json")
        for m in mapping_type:
            for a in algorithm:
                print(u, m, a)
                core_result = []
                for c in multicore:
                    fitness_result = dict()
                    for f in range(len(fitness_functions)):
                        r = make_multicore_scheduling(num_cores=c, mapping_type=m, u_total=u, scheduling_type=a,
                                                      fitness_function=fitness_functions[f])
                        fitness_result[fitness_functions_name[f]] = r
                    core_result.append({c: fitness_result})
                output.append({
                    'utilization': u,
                    'mapping_type': m.name,
                    'algorithm': a.name,
                    'core_result': core_result
                })
        write_output_to_file("./output_u_" + str(u) + ".json", json.dumps(output, indent=4))
