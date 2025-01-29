import multiprocessing
from src.config import settings

workers = settings.GUNICORN_WORKERS
workers_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:8000"
keepalive = 120
timeout = 30
worker_tmp_dir = "/dev/shm"