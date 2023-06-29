import random
import math


def uunifast(n, u_total):
    utilizations = []
    sum_u = u_total

    for i in range(1, n):
        next_sum_u = sum_u * math.pow(random.random(), 1 / (n - i))
        utilizations.append(sum_u - next_sum_u)
        sum_u = next_sum_u

    utilizations.append(sum_u)
    return utilizations


def check_condition(utils, core_num):
    for i in utils:
        if i > core_num:
            return False
    return True


def get_uunifast(n, u, core_num):
    while True:
        utilizations = uunifast(n, u)
        if core_num > 1 or check_condition(utilizations, core_num):
            return utilizations
