def min_completion_latency(task, start_time):
    latency = task.get_latency(start_time)
    completion_time = task.get_completion_time(start_time)
    fitness_score = 1 / (0.6 * completion_time + 0.4 * latency)
    return fitness_score


def min_response_wait(task, start_time):
    response_time = task.get_response_time(start_time)
    wait_time = task.get_wait_time(start_time)
    fitness_score = 1 / (0.6 * response_time + 0.4 * wait_time)
    return fitness_score


def min_wait_latency(task, start_time):
    latency = task.get_latency(start_time)
    wait_time = task.get_wait_time(start_time)
    fitness_score = 1 / (0.6 * wait_time + 0.4 * latency)
    return fitness_score


def min_response_latency(task, start_time):
    latency = task.get_latency(start_time)
    response_time = task.get_response_time(start_time)
    fitness_score = 1 / (0.7 * response_time + 0.3 * latency)
    return fitness_score


def min_completion_response(task, start_time):
    response_time = task.get_response_time(start_time)
    completion_time = task.get_completion_time(start_time)
    fitness_score = 1 / (0.6 * completion_time + 0.4 * response_time)
    return fitness_score


def min_completion_sumOfSlack(tasks, task, start_time):
    pass

def min_completion_latency_response( task, start_time):
    latency = task.get_latency(start_time)
    response_time = task.get_response_time(start_time)
    completion_time = task.get_completion_time(start_time)
    fitness_score = 1 / (0.3 * latency + 0.3 * completion_time + 0.5 * response_time)
    return fitness_score


def min_completion_sumOfSlack_response(tasks, task, start_time):
    sumOfSlack = sum([t.get_slack_time(start_time) for t in tasks])
    pass

