from ssl import RAND_pseudo_bytes
from typing_extensions import Self
from locust import HttpUser, task, constant_throughput

class HelloWorldUser(HttpUser):
    count = 1
    rps = 1
    wait_time = constant_throughput(rps)
    # fixed_count = 5000

    @task
    def from_0_to_50(self):
        while self.count <= 50:
            self.rps += 1 
            self.count += 1
            self.client.get("/test1")
            print(self.rps, self.count)
