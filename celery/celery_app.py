from celery import Celery

app = Celery(
    "demo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["tasks"]
)

app.conf.task_routes = {
    "tasks.process_order": {"queue": "orders"}
}