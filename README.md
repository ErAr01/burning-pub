# Burning pub

This application was created for load testing applications, using the example of a simple application written on FastAPI. The load goes to 3 handlers, you can adjust their value and number, as well as the target url in the locustfile.py

Before starting the test, set the save directory on the host machine in the deploy/docker-compose.yml

From root directory: docker-compose -f deploy/docker-compose.yml up --build

Test length == 5:31 minustes

 How it works:
- first linearly increasing load from 0 to 50 RPS for a minute
- then a linear load of 50 RPS for a minute
- then linearly increasing load from 50 to 150 RPS for a minute
- then linearly decreasing from 150 to 0
