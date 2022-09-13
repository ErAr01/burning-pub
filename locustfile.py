from cProfile import run
import re
from locust import HttpUser, TaskSet, task, constant_throughput, constant_pacing
from locust import LoadTestShape
import time

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/test1")
        # self.client.get("/test2")
        # self.client.get("/test3")


class WebsiteUser(HttpUser):
    wait_time = constant_throughput(1)
    tasks = [UserTasks]


class DoubleWave(LoadTestShape):
    lakmus = 0
    users = 0
    peak_one = 50
    time_peak_one = 60  # Seconds from start untill the end of peak one
    flat = 50
    time_flat = 120  # Seconds from start untill the end of flat phase
    peak_two = 150
    time_peak_two = 180  # Seconds from start untill the end of peak two

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_peak_one: # 60
            t = 60 / self.peak_one
            if self.users >= self.peak_one:
                self.users = self.peak_one
                # time.sleep(t)
            else:
                self.users += 1
                # time.sleep(t)
            return (self.users, 1)
        elif run_time < self.time_flat: # 120
            self.users = self.flat
            return (self.users, 1)
        elif run_time < self.time_peak_two: # 180
            self.users = self.peak_two
            return (self.users, 2)
            # dif = self.peak_two - self.flat # 60
            # t = 60 / dif # 0.6
            # if self.users >= self.peak_two:
            #     self.users = self.peak_two
            #     time.sleep(t)
            #     return (round(self.users), 1)
            # else:
            #     self.users += 1
            #     time.sleep(t)
            # return (self.users, 1)
        # elif self.users > 0:
        #     self.users -= 5
        #     time.sleep(3)
        #     return (self.users, 1)
        elif run_time < 335:
            if self.lakmus == 0:
                self.users -= 1
                self.lakmus = 1
                return (self.users, 1)
            elif self.lakmus == 1:
                self.lakmus = 0
                return (self.users, 1)
        else:
            return None
            
