def min_completion_latency(schedule, tasks):
    latency = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        task_latency = task.get_latency(time)
        latency += task_latency
        time += task.execution_time
        if task_latency > 0:
            time -= task_latency
    completion_time = time
    fitness_score = 1 / (0.6 * completion_time + 0.4 * latency)
    return fitness_score


def min_response_wait(schedule, tasks):
    response_time = 0
    wait_time = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        response_time += task.get_response_time(time)
        wait_time += task.get_wait_time(time)
        time += task.execution_time

    fitness_score = 1 / (0.6 * response_time + 0.4 * wait_time)
    return fitness_score


def min_wait_latency(schedule, tasks):
    latency = 0
    wait_time = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        latency += task.get_latency(time)
        wait_time += task.get_wait_time(time)
        time += task.execution_time
    fitness_score = 1 / (0.6 * wait_time + 0.4 * latency)
    return fitness_score


def min_response_latency(schedule, tasks):
    latency = 0
    response_time = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        latency += task.get_latency(time)
        response_time += task.get_response_time(time)
        time += task.execution_time
    fitness_score = 1 / (0.7 * response_time + 0.3 * latency)
    return fitness_score


def min_completion_response(schedule, tasks):
    response_time = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        task_latency = task.get_latency(time)
        response_time += task.get_response_time(time)
        time += task.execution_time
        if task_latency > 0:
            time -= task_latency
    completion_time = time
    fitness_score = 1 / (0.6 * completion_time + 0.4 * response_time)
    return fitness_score


def min_completion_sumOfSlack(schedule, tasks):
    sumOfSlack = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        task_latency = task.get_latency(time)
        sumOfSlack += task.get_slack_time(time)
        time += task.execution_time
        if task_latency > 0:
            time -= task_latency
    completion_time = time
    fitness_score = 1 / (0.6 * completion_time + 0.4 * sumOfSlack)
    return fitness_score


def min_completion_latency_response(schedule, tasks):
    latency = 0
    response_time = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        task_latency = task.get_latency(time)
        latency += task_latency
        response_time += task.get_response_time(time)
        time += task.execution_time
        if task_latency > 0:
            time -= task_latency
    completion_time = time
    fitness_score = 1 / (0.3 * latency + 0.3 * completion_time + 0.5 * response_time)
    return fitness_score


def min_completion_sumOfSlack_response(schedule, tasks):
    sumOfSlack = 0
    response_time = 0
    time = 0
    for task_id in schedule:
        task = tasks[task_id]
        task_latency = task.get_latency(time)
        sumOfSlack += task.get_slack_time(time)
        response_time += task.get_response_time(time)
        time += task.execution_time
        if task_latency > 0:
            time -= task_latency
    completion_time = time
    fitness_score = 1 / (0.3 * response_time + 0.3 * completion_time + 0.5 * response_time)
    return fitness_score
