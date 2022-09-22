from locust import HttpUser, TaskSet, task, constant_throughput
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/test1") # <-- For your handler
        self.client.get("/test2") # <-- For your handler
        self.client.get("/test3") # <-- For your handler


class WebsiteUser(HttpUser):
    wait_time = constant_throughput(1)
    host = "fast_api_app # <-- For your host
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
            else:
                self.users += 1
            return (self.users, 1)
        elif run_time < self.time_flat: # 120
            self.users = self.flat
            return (self.users, 1)
        elif run_time < self.time_peak_two: # 180
            self.users = self.peak_two
            return (self.users, 2)
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
            