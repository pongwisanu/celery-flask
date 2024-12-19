FROM celery-base:1.0

CMD ["celery", "-A", "app", "worker"]