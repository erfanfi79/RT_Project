import json


def calc_completion_time(cores):
    max_completion_time = 0
    for core in cores:
        if len(core.assigned_tasks) > 0:
            core_max_finish_time = max([task.finish_time for task in core.assigned_tasks])
            max_completion_time = max(max_completion_time, core_max_finish_time)
    return max_completion_time


def calc_avg_completion_time(cores):
    completion_times = []
    for core in cores:
        for task in core.assigned_tasks:
            completion_times.append(task.finish_time)

    return sum(completion_times) / len(completion_times)


def calc_waiting_time(cores):
    waiting_time_by_task_id = dict()
    for core in cores:
        for task in core.assigned_tasks:
            waiting_time_by_task_id[task.id] = task.waiting_time

    return waiting_time_by_task_id


def calc_avg_waiting_time(cores):
    waiting_times = []
    for core in cores:
        for task in core.assigned_tasks:
            waiting_times.append(task.waiting_time)
    return sum(waiting_times) / len(waiting_times)


def calc_total_delay(cores):
    total_delay = 0
    for core in cores:
        for task in core.assigned_tasks:
            total_delay += (task.finish_time - task.deadline)
    return total_delay


def find_delayed_tasks(cores):
    delayed_tasks_by_id = dict()
    for core in cores:
        for task in core.assigned_tasks:
            delay = task.finish_time - task.deadline
            if delay > 0:
                delayed_tasks_by_id[task.id] = delay
    return delayed_tasks_by_id


def calc_total_slack_time(cores):
    total_slack_time = 0
    for core in cores:
        for task in core.assigned_tasks:
            total_slack_time += task.slack_time
    return total_slack_time


def generate_slack_between_tasks(cores):
    slack_between_tasks = dict()
    for core in cores:
        for task_idx, task in enumerate(core.assigned_tasks):
            if task_idx == 0:
                continue
            prev_task = core.assigned_tasks[task_idx - 1]
            slack_between_tasks[f"{prev_task.id}#{task.id}"] = task.start_time - prev_task.finish_time

    return slack_between_tasks

def generate_json_output(cores, algorithm_convergence_time=0):
    output = {
        'completionTime': calc_completion_time(cores),
        'avgCompletionTime': calc_avg_completion_time(cores),
        'waitingTime': calc_waiting_time(cores),
        'avgWaitingTime': calc_avg_waiting_time(cores),
        'totalDelay': calc_total_delay(cores),
        'tasksDelays': find_delayed_tasks(cores),
        'algorithm_convergence_Time': algorithm_convergence_time,
        'totalSlackTime': calc_total_slack_time(cores),
        'slackBetweenTasks': generate_slack_between_tasks(cores)
    }

    return json.dumps(output, indent=4)
