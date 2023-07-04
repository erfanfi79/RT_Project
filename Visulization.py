import json

from matplotlib import pyplot as plt

from Core import MappingType
from Main import SchedulingType

multicore = [1, 2, 4, 8, 16, 32]
mapping_type = [MappingType.FIRST_FIT, MappingType.WORST_FIT, MappingType.BEST_FIT]
utilization = [0.1, 0.3, 0.5, 0.7, 0.9, 1]
algorithm = [SchedulingType.ABC, SchedulingType.ESA]
fitness_functions = ['min_completion_latency', 'min_response_wait', 'min_wait_latency', 'min_response_latency',
                     'min_completion_response', 'min_completion_sumOfSlack', 'min_completion_latency_response',
                     'min_completion_sumOfSlack_response']


def plot_results():
    pass


def read_result_from_file(filepath):
    with open(filepath, 'r') as json_file:
        t = json.loads(json_file.read())
        return t


def plot_cores_avgCompletionTime(u, scheduling_t):
    r = read_result_from_file('output_u_' + str(u) + '.json')

    for i in r:
        if i[algorithm]==scheduling_t.value:
            pass
    # Average completion time for different numbers of cores
    cores = [1, 2, 4, 8, 16, 32]
    completion_time = [10.2, 8.5, 6.9, 5.6, 4.8, 4.2]  # Replace with your actual data

    # Plotting the average completion time
    plt.plot(cores, completion_time, marker='o')

    # Set the axis labels and title
    plt.xlabel('Number of Cores')
    plt.ylabel('Average Completion Time')
    plt.title('Average Completion Time for Different Numbers of Cores')

    # Show the gridlines
    plt.grid(True)


if __name__ == '__main__':
    pass
