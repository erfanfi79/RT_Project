import json
import random
import matplotlib.pyplot as plt


class Task:
    def __init__(self, id, arrival_time, deadline, execution_time):
        self.id = id
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.execution_time = execution_time
        self.start_time = 0
        self.finish_time = 0
        self.waiting_time = 0
        self.response_time = 0
        self.slack_time = 0
