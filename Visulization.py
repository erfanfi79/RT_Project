import json

from matplotlib import pyplot as plt

from Core import MappingType
from Main import SchedulingType
import math

multicore = [1, 2, 4, 8, 16, 32]
mapping_types = [MappingType.FIRST_FIT, MappingType.WORST_FIT, MappingType.BEST_FIT]
utilization = [0.1, 0.3, 0.5, 0.7, 0.9, 1]
algorithms = [SchedulingType.ABC, SchedulingType.ESA]
fitness_functions = ['min_completion_latency', 'min_response_wait', 'min_wait_latency', 'min_response_latency',
                     'min_completion_response', 'min_completion_sumOfSlack', 'min_completion_latency_response',
                     'min_completion_sumOfSlack_response']


def plot_results():
    pass


def read_result_from_file(filepath):
    with open(filepath, 'r') as json_file:
        t = json.loads(json_file.read())
        return t


def plot_cores_avgCompletionTime(u):
    output = read_result_from_file('./Results/output_u_' + str(u) + '.json')

    cores = [1, 2, 4, 8, 16, 32]

    # List of fitness functions
    for mapping_type in mapping_types:
        for algorithm in algorithms:
            selected_result = None
            for result in output:
                if result['mapping_type'] == mapping_type.name and result['algorithm'] == algorithm.name:
                    selected_result = result
                    break

            completion_times = [[0 for i in range(len(cores))] for j in range(len(fitness_functions))]
            for f_fun in fitness_functions:
                for key, core_result in enumerate(selected_result['core_result']):
                    core_count = int(list(core_result.keys())[0])
                    f_index = fitness_functions.index(f_fun)
                    core_index = int(math.log2(core_count))
                    completion_times[f_index][core_index] = core_result[str(core_count)][f_fun]['avgCompletionTime']

            # Create a figure and axes
            fig, ax = plt.subplots(figsize=(10, 6))

            # Plotting the completion time for each fitness function
            for i in range(len(fitness_functions)):
                ax.plot(cores, completion_times[i], marker='o', label=fitness_functions[i])

            # Set the axis labels and title
            ax.set_xlabel('Number of Cores')
            ax.set_ylabel('Completion Time')
            ax.set_title('Completion Time for Different Fitness Functions')

            # Show the gridlines
            ax.grid(True)

            # Add a legend
            ax.legend()
            plt.title(f"{algorithm.name}-{mapping_type.name}")
            # Display the plot
            plt.savefig(f"./{algorithm.name}-{mapping_type.name}-{u}.png")


if __name__ == '__main__':
    plot_cores_avgCompletionTime(0.1)
