from cProfile import run
import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape


class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/test1")
        # self.client.get("/test2")
        # self.client.get("/test3")


class WebsiteUser(HttpUser):
    wait_time = constant(1)
    tasks = [UserTasks]


class DoubleWave(LoadTestShape):

    def tick(self):
        run_time = round(self.get_run_time())
        user_count = 0
        
        if run_time < 60:
            user_count = run_time
            return (round(user_count), 1)
        elif run_time < 120:
            return (50, 1)
        elif run_time < 180:
            user_count = run_time -12
            print(user_count)
            return (round(user_count), 2)
        elif run_time < 225:
            return (1, 4)
        else:
            return None
