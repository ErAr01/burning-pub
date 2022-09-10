from cProfile import run
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape
import math
import time

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/test1")
        # self.client.get("/test2")
        # self.client.get("/test3")

    
# class WebsiteUser(HttpUser):
#     wait_time = constant(1)
#     tasks = [UserTasks]


# class DoubleWave(LoadTestShape):
#     """
#     A shape to imitate some specific user behaviour. In this example, midday
#     and evening meal times. First peak of users appear at time_limit/3 and
#     second peak appears at 2*time_limit/3
#     Settings:
#         min_users -- minimum users
#         peak_one_users -- users in first peak
#         peak_two_users -- users in second peak
#         time_limit -- total length of test
#     """

#     min_users = 20
#     peak_one_users = 60
#     peak_two_users = 40
#     time_limit = 180

#     def tick(self):
#         run_time = round(self.get_run_time())

#         if run_time < self.time_limit:
#             user_count = (
#                 (self.peak_one_users - self.min_users)
#                 * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
#                 + (self.peak_two_users - self.min_users)
#                 * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
#                 + self.min_users
#             )
#             return (round(user_count), round(user_count))
#         else:
#             return None


class WebsiteUser(HttpUser):
    wait_time = constant(1)
    tasks = [UserTasks]


class DoubleWave(LoadTestShape):

    def tick(self):
        run_time = round(self.get_run_time())
        
        if run_time < 60:
            if run_time < 50:
                user_count = run_time // 1.2
                return(round(user_count), 1)
            else:
                return (50, 1)
        elif run_time < 120:
            return (50, 1)
        elif run_time < 180:
            user_count = run_time * (run_time * 0.3)
            return (round(user_count), 1)
        elif run_time < 222:
            return (0, 4)
        else:
            return None
