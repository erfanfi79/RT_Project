def first_fit(cores, tasks, hyper_period):
    # Assign tasks to cores using the first fit algorithm
    for task in tasks:
        assigned = False
        for core in cores:
            if core.calculate_free_time(task.arrival_time, hyper_period) >= task.execution_time:
                core.assign_task(task)
                assigned = True
                break
        if not assigned:
            print("No available core for task:", task.id)


def best_fit(cores, tasks, hyper_period):
    # Assign tasks to cores using the best fit algorithm
    for task in tasks:
        utilizations = [(core, core.calculate_free_time(task.arrival_time, hyper_period)) for core in cores]

        assigned = False
        for core, free_time in sorted(utilizations, key=lambda x: x[1]):
            if free_time >= task.execution_time:
                core.assign_task(task)
                assigned = True
                break

        if not assigned:
            print("No available core for task:", task.id)


def worst_fit(cores, tasks, hyper_period):
    # Assign tasks to cores using the worst fit algorithm
    for task in tasks:
        utilizations = [(core, core.calculate_free_time(task.arrival_time, hyper_period)) for core in cores]

        for core, free_time in sorted(utilizations, key=lambda x: x[1], reverse=True):
            if free_time >= task.execution_time:
                core.assign_task(task)
                break
            print("No available core for task:", task.id)
            break