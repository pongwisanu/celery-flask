FROM python:3-slim

RUN apt-get -y update && apt-get install -y 

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .