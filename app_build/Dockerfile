FROM --platform=linux/amd64 python:3.9-slim-buster

WORKDIR /app

COPY ./cmd /app

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000
