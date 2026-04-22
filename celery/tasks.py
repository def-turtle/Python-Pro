from celery_app import app
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "orders.log")

@app.task
def process_order(order_id, email):
    with open(LOG_FILE, "a") as f:
        f.write(f"Processing order {order_id} for {email}\n")

@app.task(name="tasks.say_hello")
def say_hello(name):
    print(f"Hello, {name}!")