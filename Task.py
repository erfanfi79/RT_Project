import json
import random
import matplotlib.pyplot as plt


class Task:
    def __init__(self, id, arrival_time, deadline, execution_time):
        self.id = id
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.execution_time = execution_time
        self.slack_time = 0
        self.start_time = 0
        self.finish_time = 0
        self.waiting_time = 0
        self.response_time = 0

    def get_response_time(self, start_time):
        return self.get_completion_time(start_time) - self.arrival_time

    def get_slack_time(self, start_time):
        return max(self.deadline - self.get_completion_time(start_time), 0)

    def get_completion_time(self, start_time):
        return start_time + self.execution_time

    def get_wait_time(self, start_time):
        return start_time - self.arrival_time

    def get_latency(self, start_time):
        return self.get_completion_time(start_time) - self.deadline
