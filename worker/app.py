import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app =Celery()

app.conf.broker_url = "redis://localhost:6379" if os.getenv("BROKER_URL") is None or os.getenv("BROKER_URL") == "" else os.getenv("BROKER_URL")
app.conf.broker_connection_retry_on_startup = True
app.conf.result_backend = "redis://localhost:6379" if os.getenv("BROKER_URL") is None or os.getenv("BROKER_URL") == "" else os.getenv("BROKER_URL")

@app.task(name="task.Add")
def Add(a=int, b=int):
    return a+b

@app.task(name="task.Multiply")
def Multiply(a=int,b=int):
    return a*b

if __name__ == "__main__":
    args = ['worker', '--loglevel=INFO']
    app.worker_main(argv=args)